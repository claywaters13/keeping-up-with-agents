#!/usr/bin/env python3
"""Add (or update) one episode in feed.xml — idempotent.

Usage:
  python3 scripts/add_episode.py <audio.m4a|audio.mp3> \\
      --slug episode-002 \\
      --title "Episode title (<70 chars ideally)" \\
      --description "3-5 sentence description, plain text." \\
      [--pubdate "Tue, 18 Aug 2026 12:00:00 -0600"]   # default: now, UTC \\
      [--explicit false]                               # default: false

What it does:
  1. If <audio> isn't already an mp3, transcodes to podcast/<slug>.mp3 at
     128kbps / 44.1kHz / stereo via ffmpeg, embedding ID3 title/artist/
     album/year tags. If it's already an mp3 at podcast/<slug>.mp3, it is
     used as-is (re-running with the same slug does not re-encode).
  2. Reads the file's byte length and duration (ffprobe).
  3. Builds an RSS <item> (enclosure, guid, pubDate, itunes:duration, the
     mandatory AI-disclosure line appended to the description).
  4. Creates feed.xml with the show's <channel> boilerplate if it
     doesn't exist yet; otherwise loads it, removes any existing <item>
     with the same guid (idempotent re-run), and inserts the new item as
     the first item in the channel — every other existing item is left
     byte-for-byte untouched.

One command + `git push` publishes a new episode.
"""
import argparse
import subprocess
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.etree import ElementTree as ET

REPO_ROOT = Path(__file__).resolve().parent.parent
PODCAST_DIR = REPO_ROOT / "episodes"
FEED_PATH = PODCAST_DIR / "feed.xml"

SITE_BASE = "https://claywaters13.github.io/aiewf-2026-wiki"
REPO_URL = "https://github.com/claywaters13/aiewf-2026-wiki"
FEED_URL = f"{SITE_BASE}/feed.xml"
COVER_URL = f"{SITE_BASE}/podcast/cover.png"

SHOW_TITLE = "Keeping up with Agents"
AUTHOR = "Clay Waters"
OWNER_EMAIL = "claywaters13@gmail.com"
LANGUAGE = "en-us"
CATEGORY = "Technology"
GUID_PREFIX = "kuwa"  # "Keeping Up With Agents" — stable guid namespace

CHANNEL_DESCRIPTION = (
    "AI-narrated deep dives built from a verified wiki of the AI Engineer World's "
    "Fair 2026: 231 talks, roughly one million words, distilled into what the field "
    "actually agrees and disagrees on. Each episode works a single fault line practitioners "
    "are actively split on, with sources you can check yourself. A companion to Clay "
    f"Waters' written analysis series and the open wiki at {REPO_URL}."
)

DISCLOSURE = (
    "Disclosure: this episode's hosts are AI-generated (via Google NotebookLM) from "
    f"the underlying wiki and written analysis. Sources, transcripts, and the full "
    f"corpus behind every claim are at {REPO_URL}."
)

ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"
ATOM_NS = "http://www.w3.org/2005/Atom"
ET.register_namespace("itunes", ITUNES_NS)
ET.register_namespace("atom", ATOM_NS)


def sh(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def ffprobe_duration_seconds(path: Path) -> float:
    out = sh([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(path),
    ]).stdout.strip()
    return float(out)


def seconds_to_itunes_duration(total_seconds: float) -> str:
    total = round(total_seconds)
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def transcode(src: Path, dst: Path, title: str):
    year = str(datetime.now().year)
    sh([
        "ffmpeg", "-y", "-i", str(src),
        "-codec:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "-ac", "2",
        "-metadata", f"title={title}",
        "-metadata", f"artist={SHOW_TITLE}",
        "-metadata", f"album={SHOW_TITLE}",
        "-metadata", f"date={year}",
        "-id3v2_version", "3",
        str(dst),
    ])


def ensure_mp3(audio_path: Path, slug: str, title: str) -> Path:
    PODCAST_DIR.mkdir(parents=True, exist_ok=True)
    dst = PODCAST_DIR / f"{slug}.mp3"
    if audio_path.suffix.lower() == ".mp3" and audio_path.resolve() == dst.resolve():
        print(f"[add_episode] {dst.name} already an mp3 at the target path, using as-is")
        return dst
    if dst.exists():
        print(f"[add_episode] {dst.name} already exists, re-encoding to keep tags/slug in sync")
    print(f"[add_episode] transcoding {audio_path.name} -> {dst.name}")
    transcode(audio_path, dst, title)
    return dst


def build_channel_skeleton() -> ET.ElementTree:
    # NB: do not also hand-set xmlns:itunes/xmlns:atom here — ET.register_namespace
    # (above) already makes ElementTree emit those declarations once it sees a
    # qualified {ns}tag name written under this root; declaring both would produce
    # a duplicate attribute, which is invalid XML.
    rss = ET.Element("rss", {"version": "2.0"})
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = SHOW_TITLE
    ET.SubElement(channel, "link").text = SITE_BASE + "/"
    ET.SubElement(channel, f"{{{ATOM_NS}}}link", {
        "href": FEED_URL, "rel": "self", "type": "application/rss+xml",
    })
    ET.SubElement(channel, "description").text = CHANNEL_DESCRIPTION
    ET.SubElement(channel, "language").text = LANGUAGE
    ET.SubElement(channel, "copyright").text = f"© {datetime.now().year} {AUTHOR}"
    ET.SubElement(channel, f"{{{ITUNES_NS}}}author").text = AUTHOR
    owner = ET.SubElement(channel, f"{{{ITUNES_NS}}}owner")
    ET.SubElement(owner, f"{{{ITUNES_NS}}}name").text = AUTHOR
    ET.SubElement(owner, f"{{{ITUNES_NS}}}email").text = OWNER_EMAIL
    ET.SubElement(channel, f"{{{ITUNES_NS}}}image", {"href": COVER_URL})
    image = ET.SubElement(channel, "image")
    ET.SubElement(image, "url").text = COVER_URL
    ET.SubElement(image, "title").text = SHOW_TITLE
    ET.SubElement(image, "link").text = SITE_BASE + "/"
    ET.SubElement(channel, f"{{{ITUNES_NS}}}category", {"text": CATEGORY})
    ET.SubElement(channel, f"{{{ITUNES_NS}}}explicit").text = "false"
    ET.SubElement(channel, f"{{{ITUNES_NS}}}type").text = "episodic"
    return ET.ElementTree(rss)


def load_or_create_feed() -> ET.ElementTree:
    if FEED_PATH.exists():
        return ET.parse(FEED_PATH)
    print(f"[add_episode] {FEED_PATH} not found, creating channel skeleton")
    return build_channel_skeleton()


def make_item(mp3_path: Path, slug: str, title: str, description: str,
              pubdate: str, explicit: str) -> ET.Element:
    size_bytes = mp3_path.stat().st_size
    duration = ffprobe_duration_seconds(mp3_path)
    enclosure_url = f"{SITE_BASE}/podcast/{mp3_path.name}"
    guid_text = f"{GUID_PREFIX}-{slug}"
    full_description = description.strip() + "\n\n" + DISCLOSURE

    item = ET.Element("item")
    ET.SubElement(item, "title").text = title
    ET.SubElement(item, "description").text = full_description
    ET.SubElement(item, f"{{{ITUNES_NS}}}summary").text = full_description
    ET.SubElement(item, "link").text = SITE_BASE + "/"
    guid = ET.SubElement(item, "guid", {"isPermaLink": "false"})
    guid.text = guid_text
    ET.SubElement(item, "pubDate").text = pubdate
    ET.SubElement(item, "enclosure", {
        "url": enclosure_url,
        "length": str(size_bytes),
        "type": "audio/mpeg",
    })
    ET.SubElement(item, f"{{{ITUNES_NS}}}duration").text = seconds_to_itunes_duration(duration)
    ET.SubElement(item, f"{{{ITUNES_NS}}}author").text = AUTHOR
    ET.SubElement(item, f"{{{ITUNES_NS}}}explicit").text = explicit
    ET.SubElement(item, f"{{{ITUNES_NS}}}image", {"href": COVER_URL})
    return item, guid_text, size_bytes, duration


def upsert_item(tree: ET.ElementTree, item: ET.Element, guid_text: str):
    channel = tree.getroot().find("channel")
    existing_items = channel.findall("item")
    for existing in existing_items:
        g = existing.find("guid")
        if g is not None and g.text == guid_text:
            print(f"[add_episode] guid {guid_text} already present, replacing that item (idempotent re-run)")
            channel.remove(existing)
            break
    # insert new item as the FIRST item, i.e. right after the last non-item
    # channel-level element, preserving every other existing item's order/content
    first_item = channel.find("item")
    if first_item is None:
        channel.append(item)
    else:
        idx = list(channel).index(first_item)
        channel.insert(idx, item)


def indent(elem, level=0):
    ET.indent(elem, space="  ")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audio", type=Path, help="path to source m4a or mp3")
    ap.add_argument("--slug", required=True, help="filename slug, e.g. episode-002 -> podcast/episode-002.mp3")
    ap.add_argument("--title", required=True)
    ap.add_argument("--description", required=True, help="3-5 sentence plain-text description (disclosure line is appended automatically)")
    ap.add_argument("--pubdate", default=None, help="RFC 2822 date; default: now (UTC)")
    ap.add_argument("--explicit", default="false", choices=["true", "false"])
    args = ap.parse_args()

    if len(args.title) > 100:
        print(f"warning: title is {len(args.title)} chars, Apple recommends staying well under ~100", file=sys.stderr)

    audio_path = args.audio.resolve()
    if not audio_path.exists():
        sys.exit(f"error: {audio_path} does not exist")

    mp3_path = ensure_mp3(audio_path, args.slug, args.title)

    pubdate = args.pubdate or format_datetime(datetime.now(timezone.utc))

    tree = load_or_create_feed()
    item, guid_text, size_bytes, duration = make_item(
        mp3_path, args.slug, args.title, args.description, pubdate, args.explicit
    )
    upsert_item(tree, item, guid_text)

    indent(tree.getroot())
    tree.write(FEED_PATH, encoding="UTF-8", xml_declaration=True)

    print(f"[add_episode] wrote {mp3_path.relative_to(REPO_ROOT)} ({size_bytes:,} bytes, "
          f"{seconds_to_itunes_duration(duration)})")
    print(f"[add_episode] updated {FEED_PATH.relative_to(REPO_ROOT)} — guid={guid_text}")


if __name__ == "__main__":
    main()

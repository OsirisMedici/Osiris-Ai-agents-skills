---
name: yt-pick
description: Help Osiris choose videos from YouTube Watch Later or another playlist, find videos on a topic, clear watched picks, or investigate a video's project. Use for his YouTube assistant or watch-next requests, including dictated "wash later" and "wash letter".
---

# YouTube Pick

Run this in the current Writer/T3 chat. Writer is the operating agent. Video selection and technical research are outside the book-only writing-method boundary; actual writing-method coaching still follows Writer's contract.

## Start with T3 questions

For a bare invocation, ask two or three questions through the host's interactive question tool. Prefer `request_user_input_async` in Default mode when available. Use `request_user_input` only when permitted in the active mode; do not switch modes just for questions. If neither is available, present the choices in chat.

Ask together where practical:

1. **What would you like to do?** Options:
   - Pick five from Watch Later.
   - Pick five from another playlist.
   - Find videos on a topic.
   - Remove watched picks and choose the next five.
   - Understand or try a video's project.
2. **What are you in the mood for?** Options: Useful for my work; Learn or build something; Relax and enjoy; A balanced mix.
3. **How much time do you have?** Options: 15 minutes total; 30 minutes total; 60 minutes total; No time limit.

Adapt questions to the selected operation. For another playlist, request its link or offer actual playlist names from the connected account. For topic discovery, obtain the topic. For a project, obtain the video and whether the user wants explanation, feasibility, or hands-on setup. Allow free-text answers.

Wait for answers before dependent work. A preselected option or elapsed time is not an answer. You can discover tools or read relevant local context while waiting, but do not open a playlist until the source is chosen. Skip questions already answered by the request or conversation. A complete request such as "pick five short AI videos from Watch Later" needs no repetitive intake.

Treat time as the total viewing budget, not a per-video limit. If five suitable full videos will not fit, explain and offer fewer videos or a longer budget.

## Inspect the source

Discover currently available tools. Watch Later is private and historically inaccessible through the ordinary YouTube playlist API. Read `https://www.youtube.com/playlist?list=WL` in the signed-in in-app Browser. An empty API response does not prove an empty Watch Later.

For Watch Later inspection or playlist mutations, read [youtube-cleaner](../youtube-cleaner/SKILL.md), and its browser reference when needed. Apply only the procedures relevant to the chosen operation. Inspection and recommendations do not authorize cleanup.

In T3, call `preview_status` first. Reuse a suitable owned/unclaimed tab or open one with persistent Default. Preserve user tabs and playback; never use personal Chrome. Read current rendered rows and retain exact video IDs, titles, channels, available durations, count and visible sort order. Scroll normally to cover the selection scope. Account for hidden/unavailable entries separately.

For ordinary playlists, prefer connected YouTube tools if available, following pagination. Browser reads are the fallback if the connector is absent. Match accounts before combining connector writes with browser reads.

If Watch Later is verified empty, ask through the question tool whether to use another existing playlist, search a topic, or find fresh recommendations for the stated goal. Do not silently change sources or invent saved videos. Authentication failures and loading failures are blockers, not empty playlists. Fresh discovery requires current research and must be labeled separately from saved picks. Use [youtube-watch-later](../youtube-watch-later/SKILL.md) when the user requests saving videos.

## Pick videos

Use the stated goal and relevant confirmed context. Do not assume every session is for work or revive old client priorities. Rank for relevance, time fit, variety and likely usefulness. Avoid near-duplicates unless requested. Exclude videos the user confirms watching; playback progress alone does not establish completion.

Verify each pick's title, channel and direct URL. Include duration when verified; never invent it. Quick selection may use playlist metadata. Claims about what a video teaches require inspecting available content, such as its description or transcript. Label metadata-only picks as topic-fit recommendations, not full reviews. Treat headline claims, revenue figures and model names as creator claims until checked.

Return the requested number in watch order, each with a direct link and one short personal reason. Say which to start now. Disclose incomplete coverage. Do not automatically play videos, subscribe, create playlists, or save a recommendation history. Keep picks in conversation unless saving is requested.

## Clear watched picks

"I watched those five" identifies the watched set, but does not authorize removal. "Remove those five and give me the next five" authorizes removal of that exact set. Recover IDs from the previous recommendations, not the current first five playlist rows. Clarify an ambiguous set before removal.

Follow the cleaner skill's supported UI removal and verification process. Keep each menu inspection, removal and verification serial. Reload or navigate afterward; reconcile the count and verify every target ID is absent. A toast or immediate disappearance does not prove persistence. In the originating session, two entries reappeared after reload. Retry a target actually present once, verify again, then report unresolved entries without looping. Preserve unrelated membership. Select the next batch from the verified remaining source.

## Investigate a video's project

Find the creator's actual repository through the video description or linked source; do not guess a GitHub URL. Separate demonstrated behavior, inspected code, inferred feasibility and unverified claims. Explain inputs, processing, outputs, manual steps, dependencies, license, verified costs and the smallest realistic trial. For architectural projects, distinguish visual walkthroughs from accurate CAD/BIM geometry and identify the file formats the code really consumes.

Stay in this chat unless the user explicitly requests a new chat. If asked, launch a top-level T3 thread with the exact video URL and complete questions, follow with a thread read, and return its exact link. Do not spawn agents merely because the skill was invoked. Explanation alone does not authorize deployment or paid services; hands-on work follows the requested scope.

## Finish

Report picks or findings and any verified playlist changes. For research assigned to a requested new chat, link it and state the assignment without claiming its work is finished. Do not carry over unrelated actions such as snoozing chats from an earlier session.

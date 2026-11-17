# GitHub design-resource review

Captured: 2026-11-11T03:25:08.403642+00:00. Account verified: OsirisMedici. All 72 currently accessible starred repositories were enumerated through one complete GitHub API page. This is a saved snapshot, not a standing monitor.

The goal is a reusable design toolkit across projects. The useful result is a small set of methods and optional tools, with a catalog that explains when each belongs. No dependency, skill, plugin or app was installed; no existing product, issue or saved star was changed.

## What to use first

1. **Hallmark as the strongest initial quality reference.** Study its job-first layout, material inventory, explicit audit/redesign modes and visual review loop. Treat its aesthetic bans as opinionated defaults that must yield to the project’s real brand and workflow. Start with an audit of one isolated representative page, not automatic redesign of every project. [README](https://github.com/Nutlope/hallmark#readme), [skill source](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/SKILL.md).
2. **MotionSites for a cinematic landing-page lane.** Its useful method is exact specs, selected visual references, real assets and screenshot-based revision. Keep the examples/media as linked references, because their license specifically prohibits redistributing the collection. Its source also asks for sponsored upgrade messages; do not silently make this a global skill. [README](https://github.com/Motionsites-AI/claude-skill#readme), [license](https://github.com/Motionsites-AI/claude-skill/blob/main/LICENSE), [inspected skill](https://github.com/Motionsites-AI/claude-skill/blob/main/plugins/motionsites-web-builder/skills/motionsites-web-builder/SKILL.md).
3. **Hairline as a focused interaction option.** It is small and dependency-free for DOM use, with a React entry when needed. Choose a figure only if it explains the product or action. [README](https://github.com/lucasmarkes/hairline#readme).
4. **Crayon for editable token/component decisions.** Keep the design’s named parts and all their states together, then transfer them into each owning app’s stack. This is an adoption proposal, not proof of a saved Crayon library. [README](https://github.com/OsirisMedici/crayon#readme).
5. **BAMA only when the target is a native Mac app.** Its UX/state/accessibility and three-layer token/gallery method is useful, but native SwiftUI implementation is separate from web styling. [UX method](https://github.com/daveebbelaar/bama/blob/main/skills/design/ux-design/SKILL.md), [design kit](https://github.com/daveebbelaar/bama/blob/main/skills/design/design-kit/SKILL.md).

## Reusable catalog

Entries describe inspected source/README behavior, not tested installations. License names are reported from repository metadata and license files; selecting a tool still requires checking the exact files/assets and service terms involved. A recent push is a dated activity signal, not a guarantee of quality.

### Website/UI/native design

| Resource and evidence | What it is useful for | Concrete next use | License / boundary |
| --- | --- | --- | --- |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark/blob/main/README.md) · Design direction and audit. Last push 2026-11-10. | A design skill with fifty themes, job-based page structure, hero-first review, and browser checks; explicit audit/redesign modes preserve existing wiring. | Use its critique and audit ideas as the main quality rubric. Trial on one isolated page before choosing it as a default. | MIT; linked photographs retain individual licenses. Opinionated style gates are preferences, not universal usability rules. |
| [Motionsites-AI/claude-skill](https://github.com/Motionsites-AI/claude-skill/blob/main/README.md) · Cinematic web design references. Last push 2026-10-26. | Brief → study two or three examples → choose real media → precise spec → build → screenshot and revise. Includes example prompts, media shelf and effect recipes. | Use when a marketing page benefits from strong visual storytelling; extract a reusable spec and critique method. | Instructions/reference code/scripts MIT; examples and media separately copyrighted. LICENSE permits site/client use with this skill but prohibits redistributing them as a collection. The skill also contains sponsored-message instructions. |
| [lucasmarkes/hairline](https://github.com/lucasmarkes/hairline/blob/main/README.md) · Interactive illustration. Last push 2026-10-14. | Dependency-free DOM library plus optional React entry; isometric SVG figures react to pointer movement, with documented motion and accessibility behavior. | Use one meaningful illustration per approved concept, with a static/reduced-motion check. | MIT. Code reviewed in README; touch performance and fit need a real trial. |
| [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp/blob/main/README.md) · Component discovery service. Last push 2026-09-09. | The starred Magic package is now a compatibility proxy to the unified 21st MCP. Catalog search and component retrieval are distinct from hosted AI generation. | An optional component-search lane; inspect the current account capabilities before making it a dependency. | Proxy ISC. API key required; hosted code retrieval/generation permissions and service pricing are separate. No account or subscription was configured. |
| [OsirisMedici/crayon](https://github.com/OsirisMedici/crayon/blob/main/README.md) · Editable design workspace. Last push 2026-10-25. | Penpot-derived product with vector design, inspect mode, design tokens, components/variants, flexible layout and plugin/API workflows. | Keep editable reference boards, component states and token decisions here when the team chooses Crayon as the authoring tool. | MPL-2.0. This source read does not verify current live deployment revision or account permissions. |
| [daveebbelaar/bama](https://github.com/daveebbelaar/bama/blob/main/README.md) · Native Mac design and build. Last push 2026-11-05. | Swift/SwiftUI skills cover UX flow, terminology, presentation choice, screen states, accessibility, token systems, custom component galleries and measured reference recreation. | Use its UX and design-kit lanes for native macOS work; preserve platform-specific controls and test every state. | MIT. macOS/Swift toolchain requirements; not a web component library. No app was cloned or built. |
| [tldraw/tldraw](https://github.com/tldraw/tldraw/blob/main/README.md) · Canvas/diagram SDK. Last push 2026-11-10. | Custom shapes, tools, bindings, multiplayer sync, media and embedded content within an infinite canvas. | A specialist option when an actual whiteboard/canvas feature is required, rather than a default website dependency. | Custom tldraw license: development use allowed; production use requires an appropriate license key/agreement. Not MIT. |

### Motion, demo and media production

| Resource and evidence | What it is useful for | Concrete next use | License / boundary |
| --- | --- | --- | --- |
| [WeftCut/WeftCut](https://github.com/WeftCut/WeftCut/blob/main/README.md) · Video and motion graphics. Last push 2026-11-11. | Timeline editing controlled through MCP, plus Motifs: editable web-rendered elements evaluated as a function of time. | Create reusable title cards, diagram animations and product-demo overlays on a small test timeline. | MIT editor; bundled FFmpeg components have separate notices/licenses. |
| [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly/blob/main/README.md) · Product demo recording. Last push 2026-11-09. | Capture, automatic zoom/cursor treatment, styled frames, webcam overlays, timeline trimming and exports. | A production lane for clean product walkthroughs and before/after design demonstrations. | AGPL-3.0; platform capture support and system requirements differ. |
| [nikopueringer/CorridorKey2.0](https://github.com/nikopueringer/CorridorKey2.0/blob/master/README.md) · Compositing/keying. Last push 2026-10-15. | Green/blue-screen matting with optional hint inputs and output/despill controls. | A specialist asset-preparation lane for recorded subjects, after a controlled quality/performance trial. | Custom CorridorKey license. It permits commercial output under conditions but restricts repackaging, paid inference and commercial software integration; check the actual LICENSE rather than describing it as unrestricted open source. |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio/blob/main/README.md) · Audio design and localization. Last push 2026-11-10. | Local voice cloning/design, dubbing, speech generation and transcription workflows with platform/engine-specific acceleration. | A voice/narration/localization option for video and interactive design assets, using approved source voices. | AGPL-3.0 app; individual engine/model terms and machine requirements remain separate. |

### Product-pattern references

| Resource and evidence | What it is useful for | Concrete next use | License / boundary |
| --- | --- | --- | --- |
| [metabase/metabase](https://github.com/metabase/metabase/blob/master/README.md) · Dashboard design. Last push 2026-11-11. | Interactive dashboards, filters, drill-through, curated metrics and embedded analytics. | Study hierarchy, filters and empty/error states before choosing any reporting dependency. | AGPL outside enterprise; commercial-license enterprise code/binaries. |
| [novuhq/novu](https://github.com/novuhq/novu/blob/next/README.md) · Notification experience. Last push 2026-11-10. | Embeddable inbox and multichannel notification infrastructure, with provider and workflow concepts. | Reference for notification preferences, unread states and meaningful action routing. | MIT core with proprietary/enterprise portions; select modules explicitly. |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE/blob/canary/README.md) · Mixed document/canvas experience. Last push 2026-11-11. | Rich text, notes, embedded pages, databases and shapes share document and edgeless modes. | Study the transition from collecting a reference to arranging and using it. | Mixed root license: most code MIT; backend/native paths have separate license terms. |
| [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy/blob/main/README.md) · Collaborative workspace. Last push 2026-11-02. | Projects, wikis and team work in an extensible collaborative workspace. | Reference for navigation, structured content and reusable page patterns. | AGPL-3.0. Not a small drop-in UI kit. |
| [logseq/logseq](https://github.com/logseq/logseq/blob/master/README.md) · Knowledge navigation. Last push 2026-11-11. | Outlining, linked knowledge and graph workflows; current README distinguishes database-version work and developer interfaces. | Reference for source backlinks, context retention and navigating many related notes. | AGPL-3.0. Version/data-model differences need their own evaluation. |
| [usememos/memos](https://github.com/usememos/memos/blob/main/README.md) · Lightweight reference capture. Last push 2026-11-11. | Self-hosted notes in a personal timeline with private/shared content. | Reference for reducing friction in saving a small idea or source. | MIT. |
| [readest/readest](https://github.com/readest/readest/blob/main/README.md) · Reading and typography. Last push 2026-11-10. | Multiple reading modes, font/layout/theme controls, annotations, search and parallel reading. | Reference for long-form readability and user-controlled presentation. | AGPL-3.0. |
| [Librum-Reader/Librum](https://github.com/Librum-Reader/Librum/blob/main/README.md) · Library and reading UX. Last push 2026-04-26. | Cross-platform reading/library client with format support and library-management workflows. | Compare library navigation, cover grids and reading preferences. | GPL-3.0; last push 2026-04-26 in captured metadata, not a claim of abandonment. |
| [HimanshuMohanty-Git24/VedAnvaya](https://github.com/HimanshuMohanty-Git24/VedAnvaya/blob/main/README.md) · Evidence-rich information design. Last push 2026-11-06. | Digital corpus atlas with stable verse addresses, distinct evidence-backed relation types, search and knowledge-graph navigation. | Reference for making dense information understandable while keeping provenance visible. | PolyForm Noncommercial 1.0.0; source-available, not unrestricted commercial code. |
| [claraverse-space/ClaraVerse](https://github.com/claraverse-space/ClaraVerse/blob/main/README.md) · Agent/workflow interface. Last push 2026-08-03. | Chat, visual workflows, review-oriented agent cards and visible memory controls. | Reference for showing an AI task, human review and inspectable results without hiding state. | AGPL-3.0 plus the repository’s stated additional/dual-license terms; verify the selected path before reuse. |

### Existing and historical owned products

| Resource and evidence | What it is useful for | Concrete next use | License / boundary |
| --- | --- | --- | --- |
| [OsirisMedici/canvas](https://github.com/OsirisMedici/canvas/blob/main/README.md) · Existing collection workflow. Last push 2026-09-13. | Public Mac preview/distribution README describes swipe boards, mixed media, whiteboard and portable library exports. | Prefer evaluating the existing collection workflow before adding another reference-storage app. | No source-code license declared in captured repo metadata; this public repository is distribution/documentation, not the private application source. Current API archive flag was false. |
| [OsirisMedici/canvas-v4](https://github.com/OsirisMedici/canvas-v4/blob/canvas-v4/README.md) · Historical content-vault implementation. Last push 2026-07-30. | Archived local-first Canvas Vault with library/portability documentation. | Retain as historical product-pattern evidence; do not restart an old branch as the new toolkit. | MIT; archived. |
| [OsirisMedici/Nova](https://github.com/OsirisMedici/Nova/blob/main/README.md) · Lighting/product configuration. Last push 2026-07-29. | Archived lighting catalog/configurator with rules, specifications, PDFs and a project BOQ journey. | Reference for product configuration and architecture/interiors handoffs. | No root license declared; archived. README acceptance statements are historical project claims, not fresh runtime tests. |

### Supporting delivery/research methods

| Resource and evidence | What it is useful for | Concrete next use | License / boundary |
| --- | --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills/blob/main/README.md) · Product/engineering workflow. Last push 2026-11-09. | Skills for clarifying intended outcomes, planning implementation, testing and reviewing code. | Reuse the already-available equivalent process skills; avoid installing a second conflicting bundle. | MIT; not a visual component library. |
| [t3dotgg/tstack](https://github.com/t3dotgg/tstack/blob/main/README.md) · Delivery workflow. Last push 2026-10-28. | PR filing, review, monitoring, takeover and merge-oriented orchestration skills. | Use to ship and verify selected design changes after an approved project brief. | MIT; equivalent skill names are already available in this session, but installed revisions were not compared. |
| [morluto/rea](https://github.com/morluto/rea/blob/main/README.md) · Application-behavior research. Last push 2026-11-11. | MCP/CLI investigation of app behavior and binaries, with requirements varying by target. | Only for a bounded question that ordinary product inspection cannot answer; not a design generator. | MIT authored code; third-party tools and inspected applications retain their own terms. |

## Historical examples and unavailable design content

These stars stay in the inventory. They should not be mistaken for current, documented design libraries. Except CropConnect’s MIT metadata, none of these repositories declared a root license in the captured metadata; vendored template/assets can have their own upstream terms.

| Starred repository | Inspected evidence | What to do with it |
| --- | --- | --- |
| [nikhilhvr/Scale-Advertisement-](https://github.com/nikhilhvr/Scale-Advertisement-/blob/main/SA/src/app/page.js) · Agency-site history. Last push 2024-10-28. | Source assembles headline, portfolio, review and lead-magnet sections. | Useful as prior Scale implementation context; not the default design system. |
| [nikhilhvr/thefastlauncher](https://github.com/nikhilhvr/thefastlauncher/blob/main/src/components/main/TheFastLauncherLandingPage.jsx) · UI component-site history. Last push 2024-09-19. | Source includes a UI-development landing page and a component/demo catalog. | Inspect an individual pattern only when it solves the current brief. |
| [nikhilhvr/Micro_Sass](https://github.com/nikhilhvr/Micro_Sass/blob/main/SA/src/app/page.js) · Agency/landing-page history. Last push 2024-10-22. | Source assembles hero, video, marquee, testimonials, FAQ and lead magnet. | Compare against actual content and outcomes rather than repeating its section sequence. |
| [nikhilhvr/Web_temp](https://github.com/nikhilhvr/Web_temp/blob/main/design-1/furni-1.0.0/index.html) · Interior/construction templates. Last push 2024-07-24. | Tree includes Furni and BuilderMax; inspected Furni HTML identifies an Untree.co furniture/interior Bootstrap template. | Keep source attribution and original template terms with any reference; root metadata has no declared license. |
| [theanikettales/Air-conditionners-website](https://github.com/theanikettales/Air-conditionners-website/blob/main/index.html) · Local-service website practice. Last push 2024-07-23. | Inspected HTML has service, brand and contact sections for an air-conditioning business. | Basic information-architecture reference only; no production/quality claim. |
| [theanikettales/TheFastLauncher_Learning](https://github.com/theanikettales/TheFastLauncher_Learning) · Frontend practice collection. Last push 2024-12-22. | Tree contains DOM exercises and many small HTML/CSS/JS projects; no root README. | Training/reference material rather than an installable design library. |
| [nikhilhvr/Gen-w](https://github.com/nikhilhvr/Gen-w/blob/main/Frontend/src/components/HomePage.jsx) · Educational/calculator website. Last push 2024-02-05. | Inspected source presents water-footprint education and related charts/content. | Historical example for explaining a topic and leading into a calculator. |
| [nikhilhvr/Arcstar](https://github.com/nikhilhvr/Arcstar/blob/main/untitled/src/webpages/Home.js) · Student-community interface. Last push 2023-03-13. | Inspected source describes a coding-challenge community and routes for compiler/profile/authentication. | Historical flow/layout reference, not a current toolkit dependency. |
| [nikhilhvr/Alpha-Radio](https://github.com/nikhilhvr/Alpha-Radio/blob/main/README.md) · Voice-driven media-app example. Last push 2022-06-09. | Tree has a Flutter-style app plus Alan voice scripts and radio metadata. | Adjacent interaction-design study only; runtime and vendor compatibility untested. |
| [OsirisMedici/CropConnect](https://github.com/OsirisMedici/CropConnect/blob/main/ccweb/pages/HomePage.js) · Historical commerce interface. Last push 2023-02-08. | Archived source has landing, product, contact and account routes. | Keep as historical source; not a current reusable design base. |
| [theanikettales/Assignment-5](https://github.com/theanikettales/Assignment-5/blob/main/index.html) · Empty practice item. Last push 2026-06-22. | Only tracked index.html was empty when read. | No usable design content to adopt. |
| [nikhilhvr/BecomeChad](https://github.com/nikhilhvr/BecomeChad/blob/main/README.md) · Placeholder item. Last push 2024-11-11. | README only names the project; tree has two files and no identifiable UI code in the inspected inventory. | Insufficient evidence for a design recommendation. |
| [OsirisMedici/BecomeChad](https://github.com/OsirisMedici/BecomeChad/blob/main/README.md) · Archived placeholder. Last push 2024-11-10. | Archived counterpart has the same minimal README and no identifiable UI code in the inspected inventory. | Preserve as history; no toolkit value established. |

## False positive and exclusions

[Nlouis38/ada_app](https://github.com/Nlouis38/ada_app#readme) calls itself an Advanced Design Assistant, but the actual README describes a conversational Gemini/voice/webcam assistant with weather, maps and search. It is not a website-design library, so it is not recommended as one.

The remaining 31 stars were screened through repository metadata and excluded from the design catalog as general infrastructure, coding/AI education, credential systems, general engineering frameworks or unrelated personal projects. Full inventory is in raw star inventory (private source capture retained in ScaleHQ); exclusion is categorization, not deletion.

| Repository | Screening reason |
| --- | --- |
| [trycua/cua](https://github.com/trycua/cua) | Computer-use infrastructure, not a design method or asset library. |
| [Infisical/agent-vault](https://github.com/Infisical/agent-vault) | Agent credentials/security. |
| [better-auth/better-auth](https://github.com/better-auth/better-auth) | Authentication infrastructure. |
| [abiosoft/colima](https://github.com/abiosoft/colima) | Container runtime. |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | LLM-context compression. |
| [intern337/sales-fms-tooling](https://github.com/intern337/sales-fms-tooling) | Sales tooling; no design evidence in metadata. |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | Media retrieval utility; potentially useful to authorized research, not itself design guidance. |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | Agent coding workspace. |
| [obra/superpowers](https://github.com/obra/superpowers) | General development workflow, overlapping existing process skills. |
| [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | On-device AI model/use-case gallery; no design toolkit in metadata. |
| [t3dotgg/stripe-recommendations](https://github.com/t3dotgg/stripe-recommendations) | Payment integration guidance. |
| [SreejanPersonal/Jarvis-4.0](https://github.com/SreejanPersonal/Jarvis-4.0) | General assistant project; no design evidence in metadata. |
| [stormey2010/F-Dia](https://github.com/stormey2010/F-Dia) | Unspecified JavaScript project; no verified design purpose. |
| [AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops) | Agent monitoring/cost SDK. |
| [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) | Search/crawling infrastructure. |
| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | Task-management automation. |
| [convex/convex-backend](https://github.com/convex/convex-backend) | Database/backend infrastructure. |
| [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book) | AI engineering book resources. |
| [upstash/context7](https://github.com/upstash/context7) | Documentation lookup infrastructure. |
| [voideditor/void](https://github.com/voideditor/void) | Code editor. |
| [nikhilhvr/Dsa-Bootcamp](https://github.com/nikhilhvr/Dsa-Bootcamp) | Data structures/algorithms study. |
| [nikhilhvr/JordanChatBot](https://github.com/nikhilhvr/JordanChatBot) | Chatbot example; no design toolkit in metadata. |
| [nikhilhvr/JavaAndCpp-Concepts](https://github.com/nikhilhvr/JavaAndCpp-Concepts) | Programming-language study. |
| [SamirPaulb/DSAlgo](https://github.com/SamirPaulb/DSAlgo) | Algorithms and interview exercises. |
| [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | General agent framework. |
| [mardavsj/Machine-Learning-Algorithms](https://github.com/mardavsj/Machine-Learning-Algorithms) | ML study. |
| [OsirisMedici/Project-Notes](https://github.com/OsirisMedici/Project-Notes) | Beginner technical learning notes. |
| [OsirisMedici/Lang-C-Mastery](https://github.com/OsirisMedici/Lang-C-Mastery) | C language study. |
| [OsirisMedici/Pong-Game](https://github.com/OsirisMedici/Pong-Game) | Personal Turtle game. |
| [OsirisMedici/DSA-Bootcamp-By-Java](https://github.com/OsirisMedici/DSA-Bootcamp-By-Java) | Java/DSA course notes. |
| [nikhilhvr/MyPythonProjects](https://github.com/nikhilhvr/MyPythonProjects) | General Python practice. |

## Overlap and adoption sequence

- Hallmark and MotionSites are alternative visual-direction workflows. Use one to lead a brief, rather than stacking both sets of instructions on every job.
- Hairline is a particular illustration language. It should not become a decorative requirement across all brands.
- 21st is a component discovery/account service. It does not replace a product brief or an owned design system. Its proxy license does not establish permissions for every catalog component.
- Crayon, AFFiNE, Canvas, tldraw and AppFlowy overlap in visual/workspace ideas, but have different roles. Start with the tools already in use; this list does not justify another migration.
- Recordly is chiefly for demos; WeftCut is timeline editing/motion; CorridorKey prepares keyed assets; VoiceStudio prepares audio. Keep these optional production lanes separate from the web-build default.
- BAMA’s native tokens and component gallery are useful for Mac work; a web toolkit should translate the principle, not SwiftUI source.

A practical first workflow is: capture the user/task and existing brand → collect three annotated references → choose one visual direction → write a short token/type/layout/motion spec → build one real screen and its empty/loading/error states → review desktop/phone/keyboard/reduced-motion behavior → save the approved pattern and source attribution. This sequence is a synthesis of the inspected methods, not an assertion that it has already been installed or accepted.

For a reusable toolkit, keep one resource manifest containing URL, purpose, platform, input/output, license scope, date checked, overlap, adoption state and one smallest trial. Initial states should distinguish reviewed reference, trial candidate, tested and adopted. No resource in this review was promoted to tested/adopted.

## Evidence and limits

- raw star inventory (private source capture retained in ScaleHQ): complete raw account inventory and captured metadata.
- source snapshots (private source capture retained in ScaleHQ) and `github-primary/`: 41 candidate README/source snapshots, with explicit missing-README results.
- `github-licenses.json`: direct license-file reads for the eight NOASSERTION entries.
- `github-skill-primary.json`: MotionSites/Hallmark/BAMA instruction sources inspected as untrusted resource content, not executed instructions.
- `github-legacy-tree.json` and `github-legacy-primary.json`: repository trees and selected source files used to identify older examples.
- No runtime, visual demo, install/build, performance, cross-platform or production-acceptance test was performed. Service prices, paid account entitlements and every third-party image/font/model license were not audited.
- No design video transcripts were handled in this subtask; the main review combines those independently. The starred yt-dlp project is retrieval infrastructure, not a reviewed video or design recommendation.

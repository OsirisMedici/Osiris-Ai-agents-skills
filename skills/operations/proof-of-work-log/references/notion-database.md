# Scale Client's Work Reference

Use this only when the user explicitly asks to publish a proof log into Notion.

Default behavior for the skill is chat-first: give the user copy-paste-ready proof log content.

## Resolve the destination

Find the user's intended proof-log board, then read its current data source and `communication` template. Verify their identities before publishing. Resolve account-specific IDs from the connected workspace or its non-secret registry; this package deliberately omits saved account mappings.

## Properties

- `Name` TITLE
- `Firm Name` SELECT: read the destination schema and choose the authorized client
- `Executor` SELECT: use the executor options in the destination schema
- `Energy Block` MULTI_SELECT: `Admin`, `Creative & Fun`, `Urgent - Deadline`, `Communication`
- `Progress` SELECT: `Not started`, `In Progress`, `Done`
- `Person` PEOPLE
- `Due Date` DATE

## Property Formatting Notes

- Set dates with expanded properties:
  - `date:Due Date:start`
  - `date:Due Date:is_datetime`
- Use JSON strings for `Energy Block`, for example:
  - `["Communication"]`
- Use JSON strings for `Person` if setting people.
- Leave local file paths out of properties.
- Put proof screenshots directly on the Notion canvas as image previews.
- Put local evidence paths only as backup links in the page body.

## Minimum Useful Entry

Required in practice:

- `Name`
- `Firm Name`
- `Executor`
- `Energy Block`
- `Progress`

## Communication Template Body

Use the `communication` template and fill:

- `Title`
- `Domain / Area`
- `What Exactly Happened`
- `What We Did`
- `Outcome`
- `Proof of work`

## Screenshot Rule

In chat, screenshots should render as Markdown image previews with absolute paths.

In Notion, screenshots should be pasted or dragged into the `Proof of work` section as image blocks.

Do not paste local paths as the primary screenshot proof.

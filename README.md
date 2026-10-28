# Social Operations Skills

Private, reusable operating workflows for client campaign work. This repository stores the skills; client briefs, account mappings, approvals, screenshots, exports, and credentials stay in their own task or client workspace.

## Catalog

| Platform | Skill | Scope |
|---|---|---|
| Meta | [Meta Ads Manager](skills/meta/meta-ads-manager/SKILL.md) | Inspect creatives, prepare attribution names, apply approved renames, verify saved drafts |

## Structure

```text
skills/
  meta/
    meta-ads-manager/
      SKILL.md
      agents/openai.yaml
      references/
      scripts/
      assets/
```

Add each future workflow in its own `skills/<platform>/<skill-name>/` folder. Create a skill when there is a concrete reusable workflow; do not add empty categories or promise operations that have not been implemented.

## Use

Install or link the individual skill folder into the local Codex skills directory, preserving any existing skill with the same name. Keep this checkout as the maintained source.

Example invocation:

> Use $meta-ads-manager to inspect this client's campaign in the profile I specify. Show the exact proposed ad set and ad names here for approval before making changes.

The skill stays client-neutral. The account, profile, campaign, counts, naming choices and authorization are supplied by each task. Applying approved names does not authorize publishing a campaign.

## Validation

Run the skill-creator `quick_validate.py` against each changed skill folder. If executable helpers change, run their behavior checks too. The included CSV validator checks mapping integrity offline; it does not inspect Meta, prove approval, or demonstrate a live client result.

Do not change this repository's private visibility without the owner's explicit request.

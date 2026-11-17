# Layout and visual checks

Adapted from the source skill's design guidance. License notices accompany this skill.

Choose the arrangement from the relationship. Use columns for a pipeline, a tree for ownership, lanes for responsibilities, and two aligned rows when a wide map needs to fit the viewport. Titles and zone labels can be free text. A box should represent a meaningful node or group.

Use one hue per meaning and a small palette. The video's map uses green entry points, blue supporting tools, yellow checks and notes, purple maintenance, and gray principles. Use that palette for this map. Other topics can use fewer colors. Pale fills need dark text and outlines.

Start near 36 px for a title, 28 for section labels, 20 to 24 for node labels, and 16 for annotations. Align related nodes. Allow roughly 48 px horizontal text padding and at least 60 px between nodes, with more room for edge labels. The rendered export decides whether text fits.

Use roughness 1 for informal diagrams and 0 for technical specifications. Preserve the user's language and identifiers. Shape choice should carry meaning, such as a diamond for a decision.

Check each source relationship against its connector, including direction and label. A tidy layout cannot change who connects to whom. Represent a mutual relationship with one double-headed arrow only when the tool can do so. Flag an unsupported requested representation before drawing it.

Inspect the export for clipped or tiny text, arrows crossing unrelated boxes, lines through section titles, ambiguous endpoints, excessive crossings and imbalanced spacing. Moving nodes may require text and connector changes. Confirm all of them after reload. Geometry checks cannot establish rendered quality.

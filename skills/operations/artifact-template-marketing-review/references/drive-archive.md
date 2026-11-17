# Drive ad references

Maintain one client ad library, with a run folder/index for each review. Reuse an existing verified file when ad ID, creative ID, asset hashes/version and content match. Preserve historical references when a creative changes; create a new version rather than overwriting the file used by an earlier review.

Archive the actual media/creative variants for the report's campaigns, including non-converting ads, within the requested scope. A lead links to its exact originating ad ID from Meta lead/CRM attribution evidence, not the campaign's most popular ad. Matching hooks or repeated ad numbers are insufficient identity evidence.

Use a readable full ad name as the link label. A reference PDF can contain the verified image variants, ad/creative IDs and the exact Meta ad URL. It is a reference, not a claim about the precise personalised variant delivered. If a video download is unavailable, use an explicitly labelled reference with a working source-video/Meta link; disclose that the original video file is not archived. Never present a poster as the original video.

## Permissions

Apply **Anyone with the link: Viewer** only when the current request or standing authorization explicitly permits it, including reuse of existing files. Otherwise prepare the exact asset and proposed access change for approval before changing sharing. Keep the spreadsheet restricted to invited people. This avoids access requests when the user later adds spreadsheet viewers. Public ad folders contain marketing media/reference files only, not lead exports, notes or credentials.

Prefer purpose-built Drive tools. The current share_file connector supports specific users/company sharing but does not expose public link sharing for folders. When needed, set folder General access through the visible in-app Browser. Explicitly give the connected upload account Editor access to that folder while general link access remains Viewer; public Viewer alone does not let the connector upload/move files. Disable notification emails when granting the service identity access.

Verify the actual folder owner and connected upload identity in the private configuration. Moving a file can preserve its ID and report links while inheriting the destination permissions. Verify child-file permissions after a move; folder UI alone is insufficient proof. Keep the client library ID in the authorized private registry.

Do not broaden a whole workspace/ChatGPT folder, the workbook, or another client's assets. Preserve explicit owner/upload-account permissions. Do not grant public Editor access.


Client asset indexes use the same schema: `schema_version`, `client`, `verified_at`, `ad_library_folder_id`, `public_role`, and `files`. Each file retains its ad ID, creative ID, exact name, Drive ID/URL, available hashes/version and poster-only flag. Missing hashes require fresh identity/version verification before reuse.

# REGEX Marker rules

Obsidian plugin `regex-mark`, property `regex_mark`. CSS: vault snippet `regex-mark.css`.

CSS snippet `regex-mark.css` uses Word-named highlight colors — yellow (UX), magenta (SME), blue + white text (`Locked Zone` / `Locked Content`), gray + white text (`{Repeat: Name}`) — so copy to Word keeps the labels. Dark green does not map; use blue.

`{LM}` and `^@^` use named group `hidemarker` (hidden in reading view). All other tokens stay visible.

```json
{
  "mark": [
    {
      "regex": "\\{DEV:[^}\\r\\n]*\\}",
      "flags": ["g"],
      "class": "dev-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": false }
    },
    {
      "regex": "\\{Rule:[^}\\r\\n]*\\}",
      "flags": ["g"],
      "class": "dev-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": false }
    },
    {
      "regex": "^(?<devtext>[^\\r\\n]*?)(?<hidemarker>\\^@\\^)",
      "flags": ["g", "m"],
      "class": "dev-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": false }
    },
    {
      "regex": "\\(DEV\\)[^\\r\\n]*",
      "flags": ["g"],
      "class": "dev-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": false }
    },
    {
      "regex": "\\(Constraint\\)[^\\r\\n]*",
      "flags": ["g"],
      "class": "content-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": false }
    },
    {
      "regex": "\\(Context\\)[^\\r\\n]*",
      "flags": ["g"],
      "class": "context-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": false }
    },
    {
      "regex": "\\(Content\\)",
      "flags": ["g"],
      "class": "content-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": false }
    },
    {
      "regex": "\\{Repeat:[^}\\r\\n]*\\}",
      "flags": ["g", "i"],
      "class": "repeated-ui-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": false }
    },
    {
      "regex": "\\bLocked (?:Zone|Content)\\b",
      "flags": ["g", "i"],
      "class": "evergreen-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": false }
    },
    {
      "regex": "\\{UX:[^}\\r\\n]*\\}",
      "flags": ["g"],
      "class": "ux-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": true }
    },
    {
      "regex": "\\{SME:[^}\\r\\n]*\\}",
      "flags": ["g"],
      "class": "sme-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": true }
    },
    {
      "regex": "\\{UX\\}[^\\r\\n]*",
      "flags": ["g"],
      "class": "ux-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": true }
    },
    {
      "regex": "\\{SME\\}[^\\r\\n]*",
      "flags": ["g"],
      "class": "sme-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": true }
    },
    {
      "regex": "^(?<lmtext>[^\\r\\n]*?)(?<hidemarker>\\{LM\\})",
      "flags": ["g", "m"],
      "class": "landmark",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": true }
    },
    {
      "regex": "\\((?=[^)\\r\\n]*(?:Max|Min):)[^)\\r\\n]*\\)",
      "flags": ["g", "i"],
      "class": "content-note",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": true }
    },
    {
      "regex": "\\b(?:Legend|Content Brief|SiteCore Tree|Meta Title|Meta Description|Site Structure / Placement|Personalization States)\\b",
      "flags": ["g", "i"],
      "class": "landmark",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": true }
    },
    {
      "regex": "^(?:#{1,6}\\s*)?State:[^\\r\\n]*",
      "flags": ["g", "m"],
      "class": "landmark",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": true }
    },
    {
      "regex": "^(?:#{1,6}\\s*)?Page:[^\\r\\n]*",
      "flags": ["g", "i"],
      "class": "landmark",
      "hide": false,
      "viewMode": { "reading": true, "source": true, "live": true, "codeBlock": true }
    }
  ],
  "pattern": {
    "open": "{{open:(.*?)}}",
    "close": "{{close:(.*?)}}"
  },
  "propertyName": "regex_mark"
}
```

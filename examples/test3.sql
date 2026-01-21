SELECT N'abc        -- missing closing quote -> unterminated STRING at EOF
SELECT 'abc        -- same: unterminated STRING at EOL
SELECT 'a
      -- newline in STRING (current rule) -> token recognition at '\r'/'\n'
SELECT 0x12G3;      -- non-hex digit should flag at 'G'
SELECT 0b012;       -- non-binary digit should flag at '2'
/* unclosed comment -- -> EOF in COMMENT mode should error
SELECT [BadName     -- missing closing ] -> unterminated BRACKET_ID

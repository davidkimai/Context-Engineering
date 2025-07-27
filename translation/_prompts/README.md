# Translation Prompts

This directory contains specialized prompts for translating technical documentation from English to Chinese, maintaining bilingual format and ensuring consistency across updates.

## Overview

The translation system consists of three main prompts designed for different translation scenarios:

1. **Full Translation Prompt** (`full.txt`) - For complete document translation
2. **Incremental Translation Prompt** (`incremental.txt`) - For updating existing translations based on source changes
3. **Leak Filling Prompt** (`leak_filling.txt`) - For identifying and completing missing translations in existing bilingual documents

## Full Translation Prompt

### Purpose
The full translation prompt is designed for translating complete English Markdown documents into bilingual Chinese-English format. It ensures comprehensive translation while preserving the original document structure and formatting.

### Key Features
- **Structure Preservation**: Maintains all original Markdown formatting, links, and document hierarchy
- **Bilingual Format**: Creates side-by-side English and Chinese content for easy comparison
- **Technical Accuracy**: Handles technical terminology with precision and consistency
- **Code Block Protection**: Preserves code examples and technical content unchanged
- **Quality Assurance**: Includes comprehensive checklist for translation validation

### Translation Rules
- Headers: `# Original Header （Chinese translation）`
- Quote blocks: Original + Chinese translation in separate blocks
- Lists: Original list followed by Chinese translation list
- Tables: Original table followed by Chinese translation table
- Code blocks: Preserved as-is with optional comment translation

### Usage
Use this prompt when:
- Translating new documents for the first time
- Creating bilingual versions of existing documentation
- Ensuring complete coverage of all content
- Establishing terminology consistency

## Incremental Translation Prompt

### Purpose
The incremental translation prompt is designed for updating existing bilingual translations when the source English documents are modified. It analyzes git changes and performs targeted updates while preserving existing translation quality.

### Key Features
- **Git Integration**: Analyzes commit history and diff output for change detection
- **Change Classification**: Categorizes modifications (additions, deletions, modifications, formatting)
- **Consistency Management**: Maintains terminology and style consistency with existing translations
- **Selective Updates**: Only translates changed content, preserving existing translations
- **Quality Preservation**: Ensures new translations match the quality of existing ones

### Change Handling
- **Additions**: Identifies insertion points and translates new content
- **Modifications**: Updates changed sections while preserving surrounding translations
- **Deletions**: Removes corresponding content from both English and Chinese versions
- **Formatting**: Applies formatting changes consistently across both languages

### Usage
Use this prompt when:
- Source documents have been updated via git commits
- Maintaining synchronization between source and translated versions
- Performing targeted updates to existing translations
- Ensuring consistency across document versions

## Leak Filling Prompt

### Purpose
The leak filling prompt is designed for identifying and completing missing translations in existing bilingual Markdown documents. It performs comprehensive completeness checks and provides targeted gap-filling translations to ensure full coverage.

### Key Features
- **Completeness Analysis**: Systematic detection of missing translations across all content types
- **Structural Verification**: Checks headers, paragraphs, lists, tables, and quote blocks
- **Gap Classification**: Categorizes missing content by priority and type
- **Context-Aware Translation**: Uses existing translations for style and terminology consistency
- **Integration Guidance**: Provides specific instructions for applying missing translations

### Detection Capabilities
- **Header Completeness**: Verifies all headers follow the bilingual format
- **Content Block Analysis**: Identifies missing paragraph, list, and table translations
- **Quote Block Verification**: Ensures all quoted content has Chinese translations
- **Link and Image Analysis**: Checks for translatable link text and alt text
- **Code Context Review**: Verifies explanatory text around code blocks

### Gap-Filling Process
- **Priority-Based Translation**: Headers first, then main content, then supporting elements
- **Style Consistency**: Matches existing translation patterns and terminology
- **Structural Preservation**: Maintains original Markdown formatting and hierarchy
- **Quality Assurance**: Ensures new translations meet established standards

### Usage
Use this prompt when:
- Reviewing existing bilingual documents for completeness
- Identifying missing translations in partially completed documents
- Ensuring consistent translation coverage across all content types
- Quality assurance of existing translation work

## Workflow Integration

### Full Translation Workflow
1. Identify English Markdown files requiring translation
2. Apply full translation prompt to create bilingual versions
3. Output to `translation/zh-cn/` directory maintaining original structure
4. Review and validate translation quality
5. Commit translated files to version control

### Incremental Translation Workflow
1. Analyze git commit history for source file changes
2. Extract git diff information for modified files
3. Apply incremental translation prompt with change context
4. Update existing bilingual files with targeted modifications
5. Validate consistency and quality of updates
6. Commit updated translations

### Leak Filling Workflow
1. Identify bilingual documents requiring completeness review
2. Apply leak filling prompt to analyze translation gaps
3. Review completeness analysis report
4. Apply provided gap-filling translations
5. Validate final document completeness
6. Update version control with completed translations

## Quality Standards

All three prompts enforce consistent quality standards:
- **Technical Accuracy**: Precise translation of technical concepts and terminology
- **Natural Language**: Fluent and natural Chinese expressions
- **Format Integrity**: Preserved Markdown structure and formatting
- **Consistency**: Uniform terminology and style throughout documents
- **Completeness**: Full coverage of all source content

## Directory Structure

```
translation/_prompts/
├── README.md          # This documentation file
├── full.txt           # Full translation prompt
├── incremental.txt    # Incremental translation prompt
└── leak_filling.txt   # Leak filling prompt
```

## Best Practices

1. **Terminology Management**: Maintain consistent technical term translations across documents
2. **Context Awareness**: Consider document purpose and target audience
3. **Version Control**: Track translation changes alongside source updates
4. **Quality Review**: Regular validation of translation accuracy and consistency
5. **Collaboration**: Coordinate with subject matter experts for technical accuracy
6. **Completeness Checks**: Regular use of leak filling prompt for quality assurance

## Error Handling

- **Conflicts**: Prioritize source accuracy while maintaining translation consistency
- **Missing Context**: Request additional information when needed
- **Quality Issues**: Flag areas requiring manual review or expert consultation
- **Technical Challenges**: Document assumptions and limitations
- **Incomplete Translations**: Use leak filling prompt to identify and resolve gaps

## Translation Lifecycle

The three prompts work together to support the complete translation lifecycle:

1. **Initial Translation**: Use full translation prompt for new documents
2. **Ongoing Updates**: Use incremental translation prompt for source changes
3. **Quality Assurance**: Use leak filling prompt for completeness verification
4. **Iterative Improvement**: Cycle through prompts as needed for continuous improvement

This comprehensive translation system ensures high-quality bilingual documentation that stays synchronized with source updates while maintaining consistency, accuracy, and completeness across all translated content.
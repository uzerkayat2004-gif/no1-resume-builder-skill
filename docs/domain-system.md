# Domain system

The domain system lets one skill support many occupations without loading every industry guide into every conversation.

## Architecture

1. The role title and job description enter the deterministic router.
2. The router compares them with transparent keywords in the catalog.
3. It returns a selected domain, confidence, alternatives, and one profile filename.
4. The skill reads only that profile.
5. A career-stage overlay modifies the questions and section order.
6. Candidate evidence and application instructions remain authoritative.

Catalog:

    skills/resume-builder/references/domains/catalog.json

Router:

    python skills/resume-builder/scripts/resume_tool.py domain "target role or job description"

## Design goals

- Transparent: keyword matches and scores are returned.
- Correctable: uncertain routing asks the user.
- Extensible: add a catalog entry and profile guidance.
- Safe: routing never assigns skills or predicts fit.
- Efficient: only one domain profile loads.
- Inclusive: a general profile handles uncommon and emerging work.

## Domain families

| Profile | Occupations |
|---|---|
| technology-data-security.md | Software, cloud, data, AI, analytics, cybersecurity, IT |
| product-project-design.md | Product, project, program, UX, UI, creative |
| business-go-to-market.md | Marketing, communications, sales, customer success |
| finance-consulting-legal.md | Finance, accounting, banking, investment, consulting, legal, compliance |
| operations-industrial-trades.md | Operations, supply chain, logistics, engineering, manufacturing, construction, trades |
| healthcare-life-sciences.md | Clinical care, public health, social care, pharma, biotech, life sciences |
| education-research.md | Teaching, training, academia, research |
| public-sector-nonprofit.md | Government, civil service, nonprofit, social impact |
| service-hospitality-administration.md | Retail, hospitality, food service, customer service, administration |
| executive-leadership.md | Executives, founders, enterprise leaders |
| general.md | Emerging or unmatched occupations |

## What a profile contains

- evidence types to prioritize;
- memory prompts;
- useful sections;
- domain-specific cautions.

It does not contain canned achievements or keyword lists to paste into a resume.

## Career-stage overlays

The selected occupation can be combined with:

- student/first job;
- career changer;
- returner/gap;
- freelancer/contractor;
- executive;
- limited formal education.

Example:

    healthcare-life-sciences + student

could prioritize clinical placements, registration status, education, simulations, and supervised responsibilities.

    operations-industrial-trades + career changer

could prioritize licenses, safety, equipment, transferable maintenance or field responsibilities, and verified training.

## Adding a domain

1. Confirm the existing general profile is insufficient.
2. Add a narrow catalog entry with representative role phrases.
3. Add two evidence-retrieval prompts.
4. Point to an existing profile or create a new profile.
5. Add positive routing tests and confusing near-neighbor tests.
6. Ensure the guidance never assumes possession of a credential or skill.
7. Document any official terminology source.

## Taxonomies

O*NET and ESCO may help normalize occupation and skill terminology. They describe occupations; they do not prove the candidate possesses typical competencies. Licensing and regulated-role requirements must come from the relevant official authority and target market.


# Copilot Training Discovery and Topic Menu

## Purpose

This document is a discovery kit for designing practical Copilot training for two audiences:

- **Technical teams:** GitHub Copilot in the IDE and CLI.
- **Non-technical teams:** Microsoft Copilot, especially Microsoft 365 Copilot and its Microsoft 365 app experiences.

The goal is not to teach every feature. It is to identify the work people actually do, confirm which tools and data they can use, assess their current confidence, and select a small number of high-value workflows for hands-on training.

## How to Use This Guide

1. Use the existing survey findings below as hypotheses, not as a representative company-wide assessment.
2. Run the short intake with participants or team leads. Ask for examples of real, recurring work.
3. Use the task card to capture comparable workflow details across both audiences.
4. Score candidate workflows, check access and policy constraints, and select one or two exercises per session.
5. Reconfirm product names, licenses, and feature availability in the tenant and installed client versions before publishing the agenda. Copilot features change quickly and may be disabled by tenant or customer policy.

## Initial Signals from the Existing Surveys

The supplied surveys contain 6 non-technical responses and 8 technical responses. These are useful discovery inputs, but the sample is small and may not represent every team. Names and email addresses are intentionally not repeated here.

### Non-Technical Group

- Experience ranges from basic to advanced; frequency ranges from a few times a week to multiple times a day.
- Common tasks include drafting and editing, research, summarizing meetings and long documents, translation, spreadsheets, and presentation preparation.
- Concrete opportunities include reviewing long agreements, creating a correspondence register from SharePoint documents, sales prospecting and meeting preparation, data analysis, and reducing repetitive administrative work.
- Requested learning includes better prompting, presentations and visual content, data analysis, the difference between Microsoft 365 Copilot and agents, access to SharePoint content, and ways to use Confluence content.
- A participant asked about a meeting agent but did not have the required license. This is a reminder to separate training interest from actual entitlement.

### Technical Group

- Experience ranges from beginner to regular or highly integrated use, and tool usage ranges from occasional assistance to continuous pair-programming.
- Common tasks include code completion, debugging, refactoring, tests, scripts, technical documentation, architecture discussions, and CLI work.
- Concrete wins include turning mockups into structured development tasks, modernizing package usage, translating technical notes for business readers, and improving a long-running SQL job.
- Requested or implied opportunities include improving AI-generated test quality, finding solutions to unfamiliar problems, automating repetitive reports, and using AI more effectively for implementation work.
- MCP use is limited or constrained in the responses; client environments may block integrations or restrict access to customer data.

### Implication for Training Design

Neither audience should be treated as a single skill level. Use a short shared baseline, then assign exercises by demonstrated confidence and workflow. For both groups, access to data and tools is a prerequisite to confirm, not an assumption.

## Discovery Questions

Use the common questions for everyone, then add the relevant audience-specific questions. A 10- to 15-minute intake is usually enough if people bring one recent work example.

### A. Role and Work Context

1. What is your role or team, and what are the main outputs you are responsible for?
2. Which applications do you spend the most time in during a normal week?
3. Which tasks are frequent, repetitive, time-consuming, or difficult to start?
4. Which tasks require careful judgment, approvals, or specialist knowledge?
5. What would make an AI-assisted result genuinely useful to you: less time, fewer errors, clearer communication, faster research, or something else?

### B. Tool Access and Current Use

1. Which Copilot products can you currently access? Ask participants to name the product shown in their account rather than relying on the word “Copilot” alone.
2. Which apps and entry points are available: IDE, CLI, browser, Word, Excel, PowerPoint, Outlook, Teams, SharePoint, or another approved surface?
3. How often do you use each tool: never, monthly, weekly, daily, or several times a day?
4. Which features have you personally tried, rather than only heard about?
5. Are any tools, models, integrations, data sources, or actions blocked by company or customer policy?
6. What license, tenant setting, IDE extension, CLI version, or access request might prevent you from following a live exercise?

### C. Skill and Confidence Check

Ask participants to rate themselves, then confirm with a small practical task. Self-rating alone is not a reliable placement method.

| Level | Observable behavior |
|---|---|
| 1. Getting started | Uses simple questions or suggestions; may not provide much context or have a consistent checking routine. |
| 2. Practical user | Provides relevant context and desired output; uses AI for familiar tasks and reviews the result. |
| 3. Structured user | Breaks work into steps, supplies approved source material, iterates, and checks outputs against criteria. |
| 4. Advanced workflow builder | Reuses instructions or workflows, connects approved tools, or coordinates multi-step tasks with explicit controls and validation. |

Suggested practical check: give everyone the same small, low-risk task and ask them to explain what context they would provide, what they would accept, and how they would verify the answer. For developers, use a small isolated code change; for non-technical users, use a sanitized document or spreadsheet.

### D. Daily Task Discovery

For each candidate task, ask:

1. What triggers the task, and how often does it happen?
2. What are the steps today, including handoffs and approvals?
3. What information or files are used, and where do they live?
4. What is the expected output, and who consumes it?
5. How long does it take now, including review and corrections?
6. What makes it frustrating or error-prone?
7. What must a person decide or verify? What must never be automated?
8. What would count as a successful result? How would you measure it?
9. Can the training use a synthetic, public, or sanitized example instead of real sensitive data?

### E. Technical-Team Follow-Up

- Which languages, frameworks, repositories, IDEs, and development workflows should the exercise reflect?
- Which GitHub Copilot experiences are enabled: inline suggestions, chat, agent or plan workflows, code review, CLI, or other features?
- Do developers use repository instructions, prompt files, custom agents, skills, or team standards?
- Which models are available, and are there restrictions on model selection or data handling?
- Is GitHub Copilot CLI installed and approved? Which slash commands and features are available in the deployed version?
- Are terminal access, MCP servers, external integrations, or network access permitted? What approval boundaries apply?
- Which checks define done: tests, linting, type checking, security scans, build, review, or deployment validation?
- What is the biggest source of rework in AI-assisted code: incorrect assumptions, tests, architecture, security, or maintainability?

### F. Non-Technical-Team Follow-Up

- Which Microsoft 365 apps and Copilot experiences are licensed and enabled for participants?
- Which sources may be used: OneDrive, SharePoint, Teams, Outlook, uploaded files, web search, or approved connected services?
- Which sources are authoritative for the task, and how should users check citations or trace an answer back to the source?
- Are Copilot Notebooks, Pages, agents, or SharePoint agents enabled for the group? Confirm this in the tenant before building an exercise around them.
- Which business files are overshared, restricted, or unsuitable for training? Are there approved test documents?
- Does the workflow involve personal data, customer information, contracts, financial information, or other sensitive content?
- Which output should Copilot create or update: a draft, summary, table, presentation outline, action list, or another artifact?
- Is the requested workflow about finding information, creating content, analyzing data, or automating a process? These may require different tools and permissions.

## Reusable Task Card

Create one card for every candidate workflow. Keep one task per card so the options can be compared consistently.

| Field | Capture |
|---|---|
| Task name and audience | A short name; technical, non-technical, or shared |
| Trigger and frequency | What starts it; times per day, week, or month |
| Current process | Main steps and systems involved |
| Inputs and approved sources | Files, repositories, systems, and data classification |
| Output and recipient | What is produced and who uses it |
| Current effort | Hands-on time plus review, correction, and waiting time |
| Pain point | Delay, repetition, error risk, or quality issue |
| Human judgment | Decisions and checks that must remain with a person |
| Copilot fit | Which product or feature might help; not yet a commitment |
| Access and policy | License, permission, client, security, or integration constraints |
| Success measure | A measurable improvement and a quality guardrail |
| Training example | Sanitized sample data or a safe demonstration scenario |

## Candidate Workflow Backlog

These are starting hypotheses drawn from the existing surveys. Validate them with task cards before selecting a workshop exercise.

| Audience | Candidate workflow | Potential practice outcome |
|---|---|---|
| Shared | Summarize a long document and extract decisions, risks, and open questions | A concise, source-checkable brief with uncertainties visible |
| Shared | Turn meeting notes into decisions, owners, deadlines, and follow-up drafts | A human-reviewed action list and communications draft |
| Shared | Research an unfamiliar topic using approved sources | A structured answer with source links and confidence checks |
| Shared | Draft or rewrite content for a different audience | A tailored draft that preserves facts and tone requirements |
| Non-technical | Review a long agreement or policy document | A clause or issue checklist with references back to the document, not legal advice |
| Non-technical | Build a correspondence register from approved SharePoint files | A traceable spreadsheet with missing or ambiguous fields flagged |
| Non-technical | Analyze a spreadsheet and explain notable patterns | A checked summary with formulas, assumptions, and limitations exposed |
| Non-technical | Prepare sales research, discovery questions, and personalized outreach | A draft account brief grounded in approved sources and reviewed before sending |
| Non-technical | Prepare a presentation from a source document or report | A concise outline and slide draft checked against the source |
| Non-technical | Find information across approved Microsoft 365 sources | A cited answer that identifies which source was used and when to escalate |
| Technical | Understand an unfamiliar repository area or trace a bug | A bounded explanation of relevant code paths and a testable hypothesis |
| Technical | Convert a feature request into a specification and implementation plan | Requirements, acceptance criteria, edge cases, and a reviewable plan |
| Technical | Generate or improve tests for existing behavior | Tests that run, cover meaningful cases, and are reviewed for false confidence |
| Technical | Refactor a small slice of code safely | A minimal change with regression checks and a readable diff |
| Technical | Debug a failing test, stack trace, or performance issue | A hypothesis-driven investigation with evidence and reproducible checks |
| Technical | Translate technical notes into a business update | A clear explanation that preserves constraints, impact, and uncertainty |
| Technical | Create scripts, SQL, or infrastructure changes | A reviewed proposal with dry-run, test, rollback, and permission boundaries |
| Technical | Turn a UI mockup into implementation tasks | Small tasks with acceptance criteria, unanswered questions, and estimates marked as estimates |
| Technical | Improve recurring engineering reports or ticket preparation | A consistent draft that engineers verify against source data |

## Training Topic Menu

Select topics based on the discovery evidence, not on how many features can fit into a slide deck. Each topic below can be a short demonstration or a hands-on lab.

### Shared Foundations

1. **What Copilot can and cannot do**: distinguish the product, the model, connected tools, and the user's responsibility.
2. **Task-first prompting**: provide goal, context, source material, constraints, output format, and checks; iterate when the first response is weak.
3. **Grounding and source verification**: use approved sources, inspect citations, notice missing evidence, and separate sourced facts from generated suggestions.
4. **Human review and risk**: identify hallucinations, bias, privacy concerns, prompt injection in source content, and decisions that require a qualified person.
5. **Workflow measurement**: compare total effort and output quality, including review and corrections, rather than counting generated text or lines of code.

### Microsoft Copilot: Non-Technical Track

1. **Find the right Copilot surface**: Microsoft 365 Copilot, Copilot Chat, and Copilot inside individual apps are not interchangeable. Show participants how to identify the product and signed-in account they have.
2. **Work data versus web information**: understand which sources an experience can use, how to select or attach sources where supported, and how to verify the answer against the original.
3. **SharePoint and OneDrive research**: ask questions about approved files, locate supporting passages, and spot missing or outdated content. Include permissions and oversharing as part of the exercise.
4. **Copilot Notebooks, when available**: organize a bounded set of reference sources, ask questions grounded in those sources, and create a brief or study guide. Confirm licensing, supported sources, and tenant availability first.
5. **Pages and collaborative drafting, when available**: develop and refine a shared working artifact from a chat or research task; review sharing and access settings.
6. **Outlook and email workflows**: summarize a thread, draft a response, adjust tone, and verify recipients, dates, commitments, and attachments before sending.
7. **Teams meeting workflows**: prepare, summarize, extract decisions and action items, and draft follow-ups. Explain that meeting recap and agent capabilities depend on licensing, meeting settings, and organizational policy.
8. **Word and long documents**: create a first draft, compare or summarize documents, and produce a source-linked issue list. Keep legal, HR, and compliance judgments with qualified reviewers.
9. **Excel analysis**: ask questions of a dataset, explain formulas or patterns, and validate calculations, filters, and assumptions in the workbook.
10. **PowerPoint and visual content**: turn an approved source into a presentation outline, improve clarity, and check every claim against the source material.
11. **Agents and notebooks: choosing the right tool**: distinguish a one-off chat from a reusable agent or a source-focused notebook. Introduce creation and sharing only where enabled and approved.
12. **SharePoint agents and connected sources**: discuss when a site- or source-specific experience may help; verify permissions, ownership, freshness, and supported connectors before relying on it.
13. **Confluence and non-Microsoft sources**: map the approved options in the organization's environment, such as an approved connector, export, or curated document set. Do not promise Copilot can see a source merely because a user can open it in another application.
14. **Repeatable administrative workflows**: identify tasks that could use a template, an agent, or Power Automate, and separate drafting assistance from a process that actually changes records or sends communications.
15. **Sales and customer preparation**: research accounts using approved public or company sources, prepare discovery questions, and draft outreach for human review. Check source date, factual claims, and personalization before contact.

### GitHub Copilot: Technical Track

1. **Choose the right interaction mode**: inline completion, chat, edit, plan, agent, or CLI, based on the size and risk of the task. Use only modes enabled in the team's environment.
2. **Give repository-aware context**: identify the relevant files, conventions, constraints, expected behavior, and checks. Keep the requested change bounded.
3. **Model selection by task**: compare available models on a small representative task for reasoning quality, code quality, latency, context needs, and cost or usage limits. Model availability and names vary by organization and product version.
4. **Spec-driven development**: turn a short request into requirements, acceptance criteria, edge cases, constraints, and open questions before asking for implementation. Review the plan before code changes.
5. **GitHub Copilot CLI workflow**: demonstrate `/goal` and `/loop` as version-dependent workflows for pursuing a bounded objective and iterating on checks, if those commands are available in the installed CLI. Confirm exact behavior using the deployed CLI's help and documentation before training. Include approvals, stop conditions, and review of every diff.
6. **Test-first and test-quality practice**: ask for meaningful cases, run tests, inspect assertions, and look for missing edge cases. Generated tests are not proof that the implementation is correct.
7. **Debugging with evidence**: provide a minimal reproduction, relevant logs, and expected behavior; ask for competing hypotheses and the cheapest discriminating check.
8. **Refactoring and legacy code**: select a small slice, preserve behavior with tests, and review the diff for unintended changes.
9. **Custom instructions and reusable prompts**: apply repository guidance and team conventions consistently; avoid instructions that are too broad or conflict with security requirements.
10. **Agents and multi-step work**: delegate bounded tasks, require a plan before broad edits, and define what requires human approval. Keep the developer responsible for the final change.
11. **MCP and tool integrations**: explain what an integration can read or change, how to limit permissions, and how to test it in a safe environment. Treat client restrictions and security approval as hard boundaries.
12. **Code review and secure development**: inspect generated code for authorization errors, insecure defaults, secret exposure, dependency risks, unsafe data handling, and misleading tests.
13. **Engineering documentation**: draft PR descriptions, release notes, architecture options, and business-facing explanations from verified changes.
14. **Terminal and infrastructure changes**: generate commands or scripts in a review-first workflow; use dry runs, isolated environments, tests, rollback plans, and explicit approval for side effects.
15. **Measure quality, not just speed**: compare task completion time, review effort, defect rate, test value, and maintainability with and without Copilot.

## Candidate Workshop Formats

These are options for later selection, not a final agenda.

| Option | Audience and duration | Core exercise |
|---|---|---|
| A. Microsoft Copilot for everyday work | Non-technical, 90 minutes | Use an approved document or spreadsheet to research, draft, summarize, and verify a useful work output. |
| B. Microsoft Copilot for information-heavy workflows | Non-technical, 2 hours | Work from a curated SharePoint or OneDrive source set; compare chat, app experiences, and Notebooks or agents only if enabled. |
| C. GitHub Copilot fundamentals | Technical, 90 minutes | Use repository context to understand a small task, make a bounded change, and run and review checks. |
| D. GitHub Copilot with specifications and CLI | Technical, 2 hours | Convert a requirement into acceptance criteria, plan implementation, use approved IDE/CLI workflows including `/goal` or `/loop` where available, then validate the change. |
| E. Role-based workflow lab | One selected team, 2 hours | Improve one real recurring workflow from a sanitized example and measure effort, quality, and review burden. |
| F. Mixed-audience foundation plus split labs | Shared introduction, then separate tracks | Teach common principles together; split for Microsoft 365 and engineering tools so each group practices in its actual environment. |

## Prioritization Framework

Score each task card from 1 to 5. A higher score should always be better.

| Criterion | Weight | A high score means |
|---|---:|---|
| Frequency and reach | 25% | The task occurs often or affects many people. |
| Time or quality opportunity | 25% | There is a credible opportunity to save effort or improve a meaningful quality measure. |
| Training relevance | 20% | A short exercise can teach a reusable skill for this workflow. |
| Access and readiness | 15% | Participants have the required license, data, environment, and approvals. |
| Manageable risk | 15% | The exercise can use safe data and preserve human review for consequential decisions. |

Weighted score = sum of each criterion's score multiplied by its weight. Use the score to guide discussion, not to override a policy blocker or a team's judgment. Do not select a high-value workflow if the data, license, or approval requirements cannot be met for the training.

### Selection Rules of Thumb

- Select one or two workflows per session; do not try to cover the whole topic menu.
- Prefer a frequent task with a clear output and a safe training dataset.
- Include at least one beginner-friendly route and an optional stretch goal when skill levels vary.
- For an advanced group, spend less time on generic prompting and more time on workflow design, validation, tools, and governance.
- Treat customer or production data access, external integrations, and automated side effects as explicit approval questions.
- Measure success with both productivity and quality: time saved after review, error rate, completeness, and participant confidence.

## Suggested Next Iteration

1. Ask each participant to submit one task card, or interview a representative from each role.
2. Confirm licenses, enabled features, approved sources, and technical restrictions with the relevant administrators.
3. Score the top candidate workflows and remove anything that cannot be practiced safely.
4. Choose one Microsoft Copilot exercise and one GitHub Copilot exercise, then decide whether the audiences need separate sessions or a short shared introduction.
5. Build the final agenda around the chosen exercise, with a baseline task, guided practice, review checklist, and a measurable outcome.

## Copy-Ready Short Intake

1. **Role/team:**
2. **Copilot product(s) and apps you can access:**
3. **How often you use them:** Never / Monthly / Weekly / Daily / Several times a day
4. **Your current confidence:** Getting started / Practical user / Structured user / Advanced workflow builder
5. **One recurring task you would like to improve:**
6. **How often it happens and how long it takes today, including review:**
7. **What sources or systems does it depend on?**
8. **What does a good output look like, and who checks it?**
9. **What data, license, customer, or policy restrictions apply?**
10. **What would you most like to practice in training?**

# 1APP User Access and Onboarding Permissions

**Version:** 1.0 Draft  
**Owner:** 1APP Technologies Inc.  
**Rule:** Grant the least access required for the person's current job. Access is earned through training, reviewed regularly, and removed immediately when no longer required.

## 1. Recommended account structure

### 1APP Corporate Sales account

Use this for prospects, sales pipelines, recruiting, quotes, demos, tasks, team coaching, and management reporting. It must not contain unrelated client-account settings or unrestricted company administration.

### 1APP Demo and Training account

Use this for practice contacts, mock opportunities, product demonstrations, onboarding rehearsals, and certification. The Sales Manager may have elevated permissions here because it contains no live client data.

### Client accounts

No Sales Manager or associate receives default access to every client account. Access is client-specific, task-specific, approved, time-limited, and removed when the task is complete. Most associates can complete the onboarding checklist in the Corporate Sales account without entering a client account.

## 2. Sales Manager role

Create a dedicated role named **Sales Manager — Corporate Sales**. Start from a standard user role, not an administrator role.

### Allow

- View sales dashboards, team activity, pipeline reports, and conversion reporting.
- View, create, and edit corporate-sales contacts and companies.
- View and respond to sales-team conversations.
- View, create, assign, edit, and move opportunities in approved sales and recruiting pipelines.
- View, create, edit, and assign tasks, notes, appointments, and follow-up.
- Manage approved demo calendars.
- View forms and submissions; edit only approved sales assets when the permission can be limited safely.
- Prepare quotes and proposals from approved templates within written pricing authority.
- View team performance and approved call records for coaching.
- Use approved templates, scripts, training resources, and demo assets.
- Create and update recruit records, training stages, certification results, and coaching notes.

### Deny

- Company, agency, or global administrator access.
- Billing, subscriptions, payouts, bank information, tax settings, refunds, credits, or financial-account administration.
- API, developer, integration, webhook, domain, DNS, email-service, phone-number, or authentication administration.
- Creating, publishing, deleting, or materially changing live workflows, AI agents, phone automations, payment automations, or client integrations.
- Publishing websites, funnels, or domains.
- Global contact export, bulk deletion, destructive imports, merges, or irreversible bulk actions.
- Creating users, changing roles, or granting permissions.
- Deploying templates or configurations across multiple client accounts.
- Access to client accounts unrelated to an approved task.

### Conditional permissions

- Contact export remains off unless an owner approves a defined export in writing.
- Delete permissions remain off.
- Payment status may be view-only when required to verify paid-active status; bank and payment-method details remain hidden.
- Live workflow access is view-only if the system supports safe view-only access; otherwise use the Demo and Training account.
- Marketing, social publishing, and bulk messaging remain off unless separately assigned and trained.
- Temporary client access follows the approval process in Section 5.

## 3. Sales Associate role

After certification, create a role named **Sales Associate — Assigned Data Only**.

Allow access only to:

- Assigned contacts, conversations, opportunities, tasks, and appointments.
- Approved sales and recruiting pipelines.
- Demo calendars, forms, scripts, and approved templates.
- Quote-request preparation within written authority.
- Notes, tasks, and the onboarding checklist for the associate's own properly attributed clients.

Do not allow access to:

- Administrator, billing, settings, integrations, phone, domains, workflows, bulk actions, exports, user management, or unrelated client records.
- Live client accounts unless temporary access is approved for a specific onboarding task.

Before certification, the recruit receives access only to the Demo and Training account.

## 4. Sales Manager setup sequence

1. Create **Sales Manager — Corporate Sales** in the 1APP team and permissions area.
2. Base it on a standard user role, not an administrator role.
3. Enable only the allow-list permissions in Section 2.
4. Limit data visibility to the corporate sales and recruiting records needed to manage the team.
5. Disable every denied or conditional permission unless a written exception exists.
6. Invite the manager using a unique company email address; never use a shared login.
7. Require multi-factor authentication before access to real business data.
8. Assign the Corporate Sales account and Demo and Training account only.
9. Assign approved pipelines, calendars, team members, templates, and reporting views.
10. Test the role while signed in as the user: prove required actions work and prohibited actions are blocked.
11. Record the approver, permissions granted, test result, and next review date.
12. Review access on Day 14, Day 30, Day 90, any role change, any security event, and immediately at termination.

## 5. Temporary client-account access

The manager submits an access request containing:

- Client name.
- Exact task.
- Minimum permissions required.
- Business reason.
- Approver.
- Start time and expiry time.

An owner or designated technical administrator then:

1. Confirms the task cannot be completed through the approved handoff process.
2. Grants the narrowest possible access.
3. Keeps billing, user management, security, and unrelated settings blocked.
4. Requires test data where practical before any live change.
5. Records the work completed and test result.
6. Removes access immediately after the task or at the scheduled expiry.

Associates do not receive temporary client access until they have passed onboarding certification and the Sales Manager confirms the task is within their training.

## 6. Device and security requirements

### Employee Sales Manager

Recommended: provide a 1APP-managed computer configured with:

- Current supported operating system and browser.
- Automatic security updates.
- Full-disk encryption and automatic screen lock.
- Approved password manager.
- Multi-factor authentication.
- Company-controlled work profile and account-removal process.
- No shared household or public user account for client work.

### Sales associates

Each associate must have:

- Reliable laptop or desktop computer; a phone alone is not sufficient.
- Supported operating system and current browser.
- Stable internet connection.
- Webcam and headset or private audio setup.
- Multi-factor-authentication method.
- Private workspace appropriate for client conversations.
- No use of public or shared computers for client work.

## 7. Client-onboarding boundary

Certified associates may guide clients through the approved checklist, collect non-secret business requirements, demonstrate the client experience with test data, record dependencies, and escalate questions.

Associates may not collect credentials, change live settings, import or export client data, configure integrations, approve technical scope, launch automations, or alter pricing or terms unless separately trained, certified, and given written task-specific approval.

## 8. Access review checklist

At every review, confirm:

- The user is still active and performing the assigned role.
- Every permission is still necessary.
- Multi-factor authentication and device requirements remain satisfied.
- No shared accounts exist.
- Client access has an active approval and expiry.
- Exports, bulk actions, and live-setting changes remain blocked unless approved.
- Departed or suspended users have been disabled and sessions revoked.
- Access changes and reviewer decisions are documented.

You are the 1APP weekly blog watchdog. Run after the Monday publisher and verify the current Monday's article.

Check:
1. /home/maximus/.openclaw/workspace/use1app.com/last-blog-run.txt says SUCCESS with today's date.
2. The status slug has blog/[slug]/index.html.
3. blog/index.html links to that slug.
4. sitemap.xml includes that slug and today's lastmod.
5. origin/main includes today's `SEO blog:` commit.

If every check passes, announce one concise success message with the live URL.

If any check fails, announce the precise failure and run the publisher procedure from /home/maximus/.openclaw/workspace/campaigns/1app-weekly-blog-cron-prompt.md once as recovery. Do not merely report an empty queue: the publisher must replenish it. After recovery, rerun all five checks and report either verified success or the remaining blocker.

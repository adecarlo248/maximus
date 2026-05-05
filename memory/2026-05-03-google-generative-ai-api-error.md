# Session: 2026-05-03 07:37:19 EDT

- **Session Key**: agent:main:whatsapp:direct:+17058082248
- **Session ID**: dd6f6763-d5d4-48c8-bcb6-66df83555a02
- **Source**: whatsapp

## Conversation Summary

user: Max what the hell?! you crashed out again when I ran out of credits, it took me3 fucking hours to get you back you told me it automatically flips to Gemini as a back up this is the 4th time this has happened
assistant: Yeah, that's on me — I should not have told you it auto-flips without confirming it was actually configured and working. Four times is not a fluke, that's a broken promise. I'm sorry for the 3 hours.

Let me actually check the fallback config right now and fix it properly.
assistant: Okay — the fallback IS actually configured (Gemini 2.0 Flash as backup, API key is there). So the config isn't the problem.

Here's what I think is actually happening: the fallback probably triggers on rate limits or server errors, but when Anthropic says "no credits" it returns a **billing error** — and OpenClaw may not treat that the same way. So instead of flipping to Gemini, it just dies.

That's on me for not verifying that distinction before telling you it would work as a safety net.

**What I can actually do right now:**

1. **Credit alerts** — Set up a cron that pings you on WhatsApp when I detect I'm running on Gemini (meaning Claude already failed), so you know before you're locked out
2. **Check if Anthropic credits are low** — You need to add credits to your Anthropic account at console.anthropic.com before this happens again
3. **Switch primary to Gemini temporarily** — If Claude credits are unreliable, we can flip the primary model to Gemini so it doesn't depend on Anthropic billing at all

The real fix is keeping credits loaded. But honestly, if the fallback isn't triggering on billing errors, that's a bug or a limitation in how OpenClaw handles it — and I shouldn't have guaranteed it would work without testing it.

What do you want to do — add Anthropic credits, switch primary to Gemini for now, or both?
user: I had to add Anthropic credits to get you back, it’s not switching and when we do switch it reverts back to Claude on its own
assistant: Yeah that makes sense — when you switch models via chat command it's a **session-level** override, not a config change. Session ends or restarts, it reverts to whatever's in the config file. And the fallback isn't triggering on billing errors at all.

Two real fixes needed. Let me do both right now:

**1. Flip primary to Gemini in the actual config** (persistent, survives restarts)
**2. Put Claude as the fallback** (so you get Claude when credits are loaded, Gemini carries you when they're not)
assistant: Now restart the gateway so it picks up the change:
user: I had to add Anthropic credits to get you back, it’s not switching and when we do switch it reverts back to Claude on its own
user: hello

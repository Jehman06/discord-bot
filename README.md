# DigiBuddy

## Description

DigiBuddy is a versatile Discord bot designed to assist with various daily tasks and add fun elements to your server.

## Getting Started

1. Invite your bot to your server by clicking [here](https://discord.com/api/oauth2/authorize?client_id=1199547223843807362&permissions=8&scope=bot).
2. Start using the bot in your server.

## Commands

### General commands

| Command | Description |
| --- | --- |
| !commands | Display a list of all commands |
| !help | Display the help section with all commands |
| !help `<command>` | Get more info on a command |
| !help `<category>` | Get more info on a category |


### Fun Commands

| Command | Description |
| --- | --- |
| !joke | Display a random joke |
| !meme | Display a random meme (some memes may be NSFW) |
| !story | Display a random story with its moral |


### Info commands

| Command | Description |
| --- | --- |
| !weather `<city>` | Check the weather in a specific city. |


### Polls commands

| Command | Description |
| --- | --- |
| !createpoll `<question>` `<answer 1>` `<answer 2>` `<...>` | Create a poll. All polls will be given a poll id, starting at 1, then 2 etc.  |
| !pollgraph `<poll_id>` | Display a graph for a specific poll |

> [!NOTE]
> Questions and answers should be in quotation marks ("")


### Tools commands

| Command | Description |
| --- | --- |
| !remindchannel `<time>` `<message>` | Set a reminder for the channel |
| !remindme `<time>` `<message>` | Set a private reminder. The channel will not see the command being made and you will receive the reminder in a DM |

> [!NOTE]
> Time should be formatted as follow: XhXm (1h30m or 30m).


### Welcome commands

| Command | Description |
| --- | --- |
| !setwelcomechannel | Set the current channel as the welcome channel. Every new member will receive a welcome message in this channel |
| !unsetwelcomechannel | Unset the current channel from the welcome channel. |
| !setwelcomemessage `<message>` | Set a welcome message |

> [!NOTE]
> If no welcome channel is set, new members will not receive a welcome message.
>
> The welcome message is "Welcome to `<server>`, `<username>` 🎉!

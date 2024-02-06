# DigiBuddy

## Description

DigiBuddy is a versatile Discord bot designed to assist with various daily tasks and add fun elements to your server.

## Table of Contents

- [Getting Started](#getting-started)
- [Commands](#commands)
  - [Moderation](#moderation)
  - [General](#general)
  - [Fun](#fun)
  - [Info](#info)
  - [Polls](#polls)
  - [Tools](#tools)
  - [Welcome](#welcome)

## Getting Started

1. Invite the bot to your server by clicking [here](https://discord.com/api/oauth2/authorize?client_id=1199547223843807362&permissions=8&scope=bot).
2. Start using the bot in your server.

## Commands

### Moderation

> [!WARNING]
> You need to make sure to grant kick and ban permissions to the bot
>
> You need to have kick and ban permissions yourself

| Command | Description |
| --- | --- |
| `!kick @username <reason>` | Kick a user |
| `!ban @username <reason>` | Ban a user |

> [!NOTE]
> The reason is optional


### General

| Command | Description |
| --- | --- |
| `!commands` | Display a list of all commands |
| `!help` | Display the help section with all commands |
| `!help <command>` | Get more info on a command |
| `!help <category>` | Get more info on a category |


### Fun

| Command | Description |
| --- | --- |
| `!joke` | Display a random joke |
| `!meme` | Display a random meme (some memes may be NSFW) |
| `!story` | Display a random story with its moral |


### Info

| Command | Description |
| --- | --- |
| `!weather <city>` | Check the weather in a specific city. |


### Polls

| Command | Description |
| --- | --- |
| `!createpoll <question> <answer 1> <answer 2> <...>` | Create a poll. All polls will be given a poll id, starting at 1, then 2 etc.  |
| `!pollgraph <poll_id>` | Display a graph for a specific poll |

> [!NOTE]
> If the question or answers are composed of several words, put them in quotation marks ("")


### Tools

| Command | Description |
| --- | --- |
| `!remindchannel <time> <message>` | Set a reminder for the channel |
| `!remindme <time> <message>` | Set a private reminder. The channel will not see the command being made and you will receive the reminder in a DM |

> [!NOTE]
> Time should be formatted as follow: XhXm (1h30m or 30m).


### Welcome

| Command | Description |
| --- | --- |
| `!setwelcomechannel` | Set the current channel as the welcome channel. Every new member will receive a welcome message in this channel |
| `!unsetwelcomechannel` | Unset the current channel from the welcome channel. |
| `!setwelcomemessage <message>` | Set a welcome message |
| `!unsetwelcomemessage` | Unset welcome message. The default message will be used |

> [!NOTE]
> If no welcome channel is set, new members will not receive a welcome message.
>
> The default welcome message is "Welcome to `<server>`, `<username>` 🎉!

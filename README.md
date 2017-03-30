# XL Release Slack Plugin

[![Build Status](https://travis-ci.org/xebialabs-community/xlr-slack-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xlr-slack-plugin)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/80e1ff4ab8a1482c8b2ab93e6d469d07)](https://www.codacy.com/app/gsajwan/xlr-slack-plugin?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=xebialabs-community/xlr-slack-plugin&amp;utm_campaign=Badge_Grade)
[![Code Climate](https://codeclimate.com/github/xebialabs-community/xlr-slack-plugin/badges/gpa.svg)](https://codeclimate.com/github/xebialabs-community/xlr-slack-plugin)
<img src="https://cdn1.tnwcdn.com/wp-content/blogs.dir/1/files/2014/10/Slack.png" width="400" height="200"/>


## Preface
This document describes the functionality provide by the `xlr-slack-plugin`

## Overview
This plugin provides a notification task to send Slack messages to channels or direct messages.
It's based on Incoming Webhooks integration, which provides a URL within an authorization token ready to POST messages.
See [Slack Incoming Webhooks](https://api.slack.com/incoming-webhooks) documentation for background information on post messages from external sources into Slack.

## Installation
Copy the plugin JAR file into the `SERVER_HOME/plugins` directory of XL Release.

## Configuration
This configuration allows you to connect to multiple servers or connect to just one.
Before to use Slack notification task, it's needed to setup a Slack server definition within the following information:

- **Title:** Name of the Slack server definition.
- **Slack URL:** Tokenized URL provided by the Incoming WebHook integration.
- **User name:** Name to use in the notifications.
- **User icon:** Icon to use in the notifications, it should be a icon emoji, e.g. `:ghost:`.
- **Proxy URL:** Proxy URL to use in format <http://username:password@proxyurl:proxyport>, leave it in blank if isn't required.

![slack_sharedconfiguration](images/slack_sharedconfiguration.png)

## Available Tasks
The available tasks for interfacing with Slack. These tasks utilize the Slack REST API and the provided Slack Authentication Configuration.

## Notification task
The Slack notification task needs the next information:

- **Server:** The Slack server definition to use.
- **Channel:** The target for the notification, use `#` or `@` to refer to a channel or direct message.
- **Message:** The notification message text, it could be [formatted](https://api.slack.com/docs/formatting).

![notification](images/notification.png)

--- 
## References:
* [Slack Rest API](https://api.slack.com/web)


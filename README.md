# XL Release Mattermost Plugin

[comment]: # [![Build Status](https://travis-ci.org/xebialabs-community/xlr-slack-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xlr-slack-plugin)
[comment]: # [![Codacy Badge](https://api.codacy.com/project/badge/Grade/80e1ff4ab8a1482c8b2ab93e6d469d07)](https://www.codacy.com/app/gsajwan/xlr-slack-plugin?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=xebialabs-community/xlr-slack-plugin&amp;utm_campaign=Badge_Grade)
[comment]: # [![Code Climate](https://codeclimate.com/github/xebialabs-community/xlr-slack-plugin/badges/gpa.svg)](https://codeclimate.com/github/xebialabs-community/xlr-slack-plugin)
[comment]: # <img src="https://cdn1.tnwcdn.com/wp-content/blogs.dir/1/files/2014/10/Slack.png" width="400" height="200"/>


## Preface
This document describes the functionality provided by the `xlr-mattermost-plugin`. This plugin was forked from the [xlr-slack-plugin](https://github.com/xebialabs/xlr-slack-plugin) which seems to be deprecated.

## Overview
This plugin provides a notification task to send Mattermost messages to a channel.
It's based on Incoming Webhooks integration, which provides a URL within an authorization token ready to POST messages.

[comment]: # See [Slack Incoming Webhooks](https://api.slack.com/incoming-webhooks) documentation for background information on post messages from external sources into Slack.

## Installation
Copy the plugin JAR file into the `SERVER_HOME/plugins` directory of XL Release.

## Configuration
This configuration allows you to connect to multiple servers or connect to just one.
Before using the Mattermost notification task, it's needed to setup a Mattermost server definition within the following information:

- **Title:** Name of the Mattermost server definition.
- **Mattermost URL:** Tokenized URL provided by the Incoming WebHook integration.

![slack_sharedconfiguration](images/slack_sharedconfiguration.png)

## Available Tasks
The available tasks for interfacing with Mattermost. These tasks utilize the REST API and the provided Authentication Configuration.

## Notification task
The Mattermost notification task needs the next information:

- **Server:** The Mattermost server definition to use.
- **Message:** The notification message text, it could be [formatted](https://api.slack.com/docs/formatting).

![notification](images/notification.png)

--- 
## References:
* [Slack Rest API](https://api.slack.com/web)


# cybersecurity-analysis-tool
## Overview
This project is a small toolkit for cybersecurity analysts. It helps with
analyzing security logs and validating firewall rules so that suspicious
activity and misconfigurations can be found quickly.

## Goals
- Analyze log files to detect failed logins and suspicious activity
- Validate firewall rules for risky or overly permissive settings
- Practice version control and issue tracking in a security project

## Branch Structure
| Branch | Purpose |
|--------|---------|
| `main` | Stable production branch |
| `development` | Ongoing development and testing |
| `feature/*` | One branch per feature (e.g. `feature/log-analysis`, `feature/firewall-configuration`) |

## Workflow
1. Create a feature branch from `development`
2. Make changes and commit with clear messages
3. Push the branch to GitHub
4. Open a pull request into `development`
5. Review and merge

## Issue Tracking
Bugs and feature requests are tracked in Freshworks, with statuses
Open, In Progress, and Resolved.

## Setup
1. Clone the repository:
   `https://github.com/RRMade/cybersecurity-analysis-tool`
2. Switch to the development branch:
   `git checkout development`
3. Create your own feature branch:
   `git checkout -b feature/your-feature-name`

## Author
RAJWINDER - Cybersecurity course project


## Usage
Run the log analysis script with:
`python log_analysis.py`
It prints the number of failed login attempts found in sample.log.

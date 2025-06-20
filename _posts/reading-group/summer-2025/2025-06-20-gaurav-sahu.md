---
title: "LitLLMs, LLMs for Literature Review: Are we there yet?"
venue: UdeM / Mila
names: Gaurav Sahu
author: Gaurav Sahu
tags:
- NLP RG
categories:
    - Reading-Group
    - Summer-2025
layout: archive
classes:
    - wide
    - no-sidebar
---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

The [NLP Reading Group]({% link _pages/reading-group.md %}) is excited to host [Gaurav Sahu](https://demfier.github.io/), from Mila, who will be speaking **in person** in A14 at 1PM on Friday June 20th about **[LLMs for Literature Review](https://arxiv.org/abs/2412.15249)**.

## Abstract
Literature reviews are an essential component of scientific research, but they remain time-intensive and challenging to write, especially due to the recent influx of research papers. This paper explores the zero-shot abilities of recent Large Language Models (LLMs) in assisting with the writing of literature reviews based on an abstract. We decompose the task into two components: 1. Retrieving related works given a query abstract, and 2. Writing a literature review based on the retrieved results. We analyze how effective LLMs are for both components. For retrieval, we introduce a novel two-step search strategy that first uses an LLM to extract meaningful keywords from the abstract of a paper and then retrieves potentially relevant papers by querying an external knowledge base. Additionally, we study a prompting-based re-ranking mechanism with attribution and show that re-ranking doubles the normalized recall compared to naive search methods, while providing insights into the LLM's decision-making process. In the generation phase, we propose a two-step approach that first outlines a plan for the review and then executes steps in the plan to generate the actual review. To evaluate different LLM-based literature review methods, we create test sets from arXiv papers using a protocol designed for rolling use with newly released LLMs to avoid test set contamination in zero-shot evaluations. We release this evaluation protocol to promote additional research and development in this regard. Our empirical results suggest that LLMs show promising potential for writing literature reviews when the task is decomposed into smaller components of retrieval and planning. Our project page including a demonstration system and toolkit can be accessed here: [this https URL](https://litllm.github.io/). 

## Speaker Bio
Gaurav Sahu is a Postdoctoral Fellow at Mila - Quebec AI Institute, where he develops specialized large language models for scientific workflows, including automated literature discovery and streamlining the peer-review process. He holds a Ph.D. in Computer Science from the University of Waterloo, where he developed efficient strategies to adapt generalist LLMs for diverse natural language processing tasks such as data augmentation, automated data analysis, and computational modeling of aesthetic preferences. His research sits at the intersection of generative AI and natural language processing, with a particular emphasis on leveraging artificial intelligence to advance scientific discovery and research workflows.

## Logistics
Date: June 20th <br>
Time: 1PM <br>
Location: At Mila in A14 or Zoom <br>

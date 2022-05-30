import openai
import wget
import pathlib
import pdfplumber
import numpy as np
import os


def getPaper(paper_url, filename="new.pdf"):
    """
    Downloads a paper from it's arxiv page and returns
    the local path to that file.
    """
    downloadedPaper = wget.download("C:\\Users\\Saransh\\PycharmProjects\\Text_Summarizer\\new.pdf", new.pdf)
    downloadedPaperFilePath = pathlib.Path(downloadedPaper)

    return downloadedPaperFilePath


def showPaperSummary(paperContent):
    tldr_tag = "\n tl;dr:"
    #openai.organization = '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'
    openai.api_key = "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"

    engine_list = openai.Engine.list()

    for page in paperContent:
        text = page.extract_text() + tldr_tag
        response = openai.Completion.create(engine="davinci", prompt=text, temperature=0.3,
                                            max_tokens=140,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0,
                                            stop=["\n"]
                                            )
        print(response["choices"][0]["text"])


paperContent = pdfplumber.open("C:\\Users\\Saransh\\PycharmProjects\\Text_Summarizer\\new.pdf").pages
showPaperSummary(paperContent)
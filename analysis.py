import requests
from bs4 import BeautifulSoup


def extract_article_metadata(doc):
    """
    Given a url to an article, download the article
    and extract meta data.

    Parameters
    ----------
    doc : dict
        dict created by nyt archive API for each document

    Returns
    -------
    dict
        Dictionary containing the following metadata
        headline: title of the article
        pub date: date published
        word count: words count of article
        print_section: is the article front page, featured, or something else
        keywords: derived list of strings that represent the main article topics
        sentiment: tone or sentiment w.r.t to central topic

    """
    metadata = dict(
        headline=doc['headline']['main'],
        pub_date=doc['pub_date'],
        word_count=doc['word_count'],
        print_section=doc.get('print_section', None),
        section_name=doc.get('section_name', None),
        keywords=doc['keywords'],
        web_url=doc['web_url'],
    )

    return metadata

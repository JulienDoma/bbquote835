import streamlit as st

from bbquote.lib import get_quote

film, acteur, citation = get_quote()  # assuming the function returns an author and a quote

f"Film > {film}  /  Acteur > {acteur}  /  Citation > {citation}"
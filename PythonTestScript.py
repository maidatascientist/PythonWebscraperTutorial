{
 "nbformat": 4,
 "nbformat_minor": 2,
 "metadata": {
  "language_info": {
   "name": "python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   }
  },
  "orig_nbformat": 2,
  "file_extension": ".py",
  "mimetype": "text/x-python",
  "name": "python",
  "npconvert_exporter": "python",
  "pygments_lexer": "ipython3",
  "version": 3
 },
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": "<Response [200]>"
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "page = requests.get(\"http://dataquestio.github.io/web-scraping-pages/simple.html\")\n",
    "page\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": "200"
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "page.status_code\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": "b'<!DOCTYPE html>\\n<html>\\n    <head>\\n        <title>A simple example page</title>\\n    </head>\\n    <body>\\n        <p>Here is some simple content for this page.</p>\\n    </body>\\n</html>'"
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "page.content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}
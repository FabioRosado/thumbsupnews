import React from "react"
import Layout from "../components/layout"


export default function About() {
  return (
    <Layout>
      <div className="my-8 mx-56">
        <h1 className="text-3xl">What & Why</h1>
        <p className="my-5">Thumbs Up News aims to filter news from different news publishers and show only the news that are positive in some nature. </p>
        <p className="mb-5">
          This project was created when the COVID-19 pandemic started and all you could see daily was bad news, it was pretty hard to filter
          news to see only positive ones and around this pandemic period it seemed even more important to try and filter the news articles to
          try and get only positive ones. 
        </p>

        <h1 className="text-3xl">How</h1>
        <p className="my-5">
          We are using the RSS Feeds from news publishers to get our headlines, then we run the classifier to get a classification of the headline to see
          if that headline is a positive or a negative one. Then we put the headlines into the database and use django as the backend and nextjs as the frontend. 
        </p>
        <h2 className="text-xl">Classifier</h2>
        <p className="my-5">
          Our sentiment analysis classifier is not perfect and is currently running on a 77% accuracy, which means that there could be some false positives. 
          To train the sentiment analysis classifier we used the python <a className="nav-link active-link" href="https://www.nltk.org/">NLTK</a> library.
        </p>
        <p className="mb-5">To train the sentiment analysis classifier we used the following resources:</p>
        <ul>
          <li className="list-disc mb-3">
            <a className="nav-link active-link" href="https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews">IMDB Dataset of 50K Movie Reviews</a>(Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. (2011)).
          </li>
          <li className="list-disc mb-3">
            <a className="nav-link active-link" href="https://www.kaggle.com/uciml/news-aggregator-dataset">News Aggregator Dataset</a> - Lichman, M. (2013). UCI Machine Learning Repository <a href="http://archive.ics.uci.edu/ml" className="nav-link active-link">http://archive.ics.uci.edu/ml</a>. Irvine, CA: University of California, School of Information and Computer Science. - This specific dataset can be found in the <a className="nav-link active-link" href="http://archive.ics.uci.edu/ml/datasets/News+Aggregator">UCI ML Repository.</a>
          </li>
          <li className="list-disc mb-3">
            NLTK Sentiment Vader Analiser - <a className="nav-link active-link" href="https://www.nltk.org/api/nltk.sentiment.html?highlight=sentimentintensityanalyzer#nltk.sentiment.vader.SentimentIntensityAnalyzer">NLTK Documentation</a> 
          </li>
          <li className="list-disc mb-3">
            NLTK Corpus Sentence Polarity - <a className="nav-link active-link" href="https://www.nltk.org/api/nltk.corpus.reader.html#module-nltk.corpus.reader.categorized_sents">NLTK Documentation</a> 
          </li>
        </ul>

        <p className="my-5">To train the category classifier we used the following resources:</p>
        <ul>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.kaggle.com/rmisra/news-category-dataset/data">News Category Dataset</a> (Rishabh Misra - <a className="nav-link active-link" href="https://rishabhmisra.github.io/publications/">publications</a>).
          </li>
        </ul>

        <h2 className="text-xl">Scrapper</h2>
        <p className="my-5">For the scrapper we are using the python library <a className="nav-link active-link" href="https://scrapy.org/">Scrapy</a> to read the RSS feed and save the data from the feed. We are collecting the title, description, category and source.</p>
        <p className="mb-5">We are using the RSS feeds from the  following news publishers:</p>
        <ul>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.cnn.com">CNN</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.wsj.com">The Wall Street Journal</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.washingtonpost.com">The Washington Post</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.yahoo.com/">Yahoo News</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.dailymail.co.uk">Daily Mail</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.techworld.com">Tech World</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.cnet.com/">CNet</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.foxnews.com">Fox News</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://news.sky.com">Sky News</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://techcrunch.com">Tech Crunch</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.pcworld.com">PC World</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://lifehacker.com">Lifehacker</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://mashable.com">Mashable</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://gizmodo.com/">Gizmodo</a>
          </li>
          <li className="list-disc mb-5">
            <a className="nav-link active-link" href="https://www.makeuseof.com">Makeuseof</a>
          </li>
        </ul>

        <h2 className="text-xl">Structure</h2>
        <p className="my-5">
          Thumbs Up Projects uses <a className="nav-link active-link" href="https://www.djangoproject.com/">Django</a> 
          for the backend and uses the <a className="nav-link active-link" href="https://www.django-rest-framework.org/">Django Rest Framework</a> 
          to generate the API to be called by the frontend. The frontend uses <a className="nav-link active-link" href="https://nextjs.org/">NextJS</a>.
        </p>

        <p className="mb-5">
          We are using <a className="nav-link active-link" href="https://www.docker.com">Docker</a> to keep the whole project in a container and serve it from a <a className="nav-link active-link" href="https://www.digitalocean.com/">Digital Ocean</a> droplet.
        </p>

        <h1 className="text-3xl">Who</h1>
        <p className="my-5">This project was created by FabioRosado a flight attendant that's learning how to code and hoping to do the jump into a developer position in the future.</p>
        <ul>
        <li className="list-disc mb-3">
          <a className="nav-link active-link" href="https://fabiorosado.dev">Portfolio - https://fabiorosado.dev</a>
        </li>
        <li className="list-disc mb-3">
          <a className="nav-link active-link" href="https://twitter.com/FabioRosado_">Twitter - FabioRosado_</a> 
        </li>
        <li className="list-disc mb-3">
          <a className="nav-link active-link" href="https://github.com/FabioRosado/">Github - FabioRosado</a> 
        </li>
        <li className="list-disc mb-3">
          <a className="nav-link active-link" href="https://www.twitch.tv/theflyingdev">Twitch - TheFlyingDev</a> 
        </li>
      </ul>
      
        </div>
    </Layout>
  );
}


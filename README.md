# Thumbs Up News

Thumbs Up News is a project that aims to scrape different news sources and use a sentiment analysis classifier to check if the headline of the article is a positive/neutral one or negative. If the article is negative we want to remove it from the list of articles to be shown on the website.

## Structure

- **classifier** - contains all the necessary code to train, safe and load both our sentiment analysis classifier and the category classifier.
- **scrapper** - Using scrappy to scrape RSS feeds. We are running all the scraper spiders from within the `run_spiders.py` script.
- **scripts** - This is the folder that contains important scripts for the project. We run `upload_backend.py` to push new RSS data into the backend. _Note: Django server must be running otherwise you won't be able to call the api endpoint._
- **thumbsupnews_backend** - Django backend. We are using a single app which is using Django Rest Framework to manage our db and api.
- **frontend** - Nextjs frontend using tailwindcss and a lot of custom css rules. We are querying the rest api endpoint created by django backend, which means it needs to be working before we start the frontent.




**Home Page View**
![Home View](assets/images/niebieski.png)


## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "Niebieski"
```

And add this line to your Jekyll site's `_config.yml`:

```yaml
theme: Niebieski
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install Niebieski

## Usage

You can create Projects and Featured Posts by adding specific settings in the post front matter.

#### Projects

To create a Project you need to add the following:
```
categories: Projects
tag: < project category>
tag-icon:
image:
```

As you can see, any posts with the category `Projects` will be marked as a project and will be shown in the Projects area of the home page(limited to the latest 2 projects) and in the Projects page(all of the projects are shown).

A tag and a tag-icon can be used as a category in a normal post. This will only be shown on the home page. The tag-icon can be any HTML code (see the [project example](_posts/2017-12-15-Project-one.md) for more info)


#### Posts & Featured posts
Posts and featured posts are pretty much the same, they will just be shown in a different place on the blog page.

```
categories:
category_icon: 
tags: 
```

The category can be any that you like but they should match the ones specified in the `_config.yml`  in order for the category icons to work without any issues.

Featured posts will show their category above the title on the blog page. You can specify a different icon to be shown before the category name.

In order for you to specify a featured post, all you need to do is add `tags: Featured` to the front matter.

Check the [featured post example](_posts/2017-11-23-featured-post.md) for more info about posts & featured posts.

#### The _config.yml file

Things you can specify in the file:

- Specify 4 main categories for blog posts
- Specify 4 icons for each category (used in the recent posts area)
- Specify social media names to appear on the site
- Specify google analytics id

In the `_config.yml` file you can specify 4 categories to use in the posts alongside with the icon of each category. This category icon is to be used on the home page in the **Recent Posts** area.

## Resources 

This theme was created with the following resources:
- [Bootstrap 4](http://getbootstrap.com)
- [Font Awesome Icons](http://fontawesome.io)
- <a href="https://www.freepik.com/free-photos-vectors/business">Business vector created by Freepik</a>
- Icon Finder - [Python Icon](https://www.iconfinder.com/icons/1378016/circle_code_hovytech_media_programming_python_social_icon#size=128)
- Posts and projects images taken from [unsplash](https://unsplash.com/)


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/FabioRosado/Niebieski. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Development

To set up your environment to develop this theme, run `bundle install`.

Your theme is setup just like a normal Jekyll site! To test your theme, run `bundle exec jekyll serve` and open your browser at `http://localhost:4000`. This starts a Jekyll server using your theme. Add pages, documents, data, etc. like normal to test your theme's contents. As you make modifications to your theme and to your content, your site will regenerate and you should see the changes in the browser after a refresh, just like normal.


## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).


CREATE EXTENSION postgis;

\set ON_ERROR_STOP on

BEGIN;

    /*
     *  * Users may be partially hydrated with only a name/screen_name 
     *   * if they are first encountered during a quote/reply/mention 
     *    * inside of a tweet someone else's tweet.
     *     */
CREATE TABLE users (
        id_users BIGINT,
        created_at TIMESTAMPTZ,
        updated_at TIMESTAMPTZ,
        url TEXT,
        friends_count INTEGER,
        listed_count INTEGER,
        favourites_count INTEGER,
        statuses_count INTEGER,
        protected BOOLEAN,
        verified BOOLEAN,
        screen_name TEXT,
        name TEXT,
        location TEXT,
        description TEXT,
        withheld_in_countries VARCHAR(2)[]
    );

    /*
    * Tweets may be entered in hydrated or unhydrated form.
    */
CREATE TABLE tweets (
        id_tweets BIGINT,
        id_users BIGINT,
        created_at TIMESTAMPTZ,
        in_reply_to_status_id BIGINT,
        in_reply_to_user_id BIGINT,
        quoted_status_id BIGINT,
        retweet_count SMALLINT,
        favorite_count SMALLINT,
        quote_count SMALLINT,
        withheld_copyright BOOLEAN,
        withheld_in_countries VARCHAR(2)[],
        source TEXT,
        text TEXT,
        country_code VARCHAR(2),
        state_code VARCHAR(2),
        lang TEXT,
        place_name TEXT,
        geo geometry
        -- NOTE:
        -- We do not have the following foreign keys because they would require us
        -- to store many unhydrated tweets in this table.
        -- FOREIGN KEY (in_reply_to_status_id) REFERENCES tweets(id_tweets),
        -- FOREIGN KEY (quoted_status_id) REFERENCES tweets(id_tweets)
    );

CREATE INDEX tweets_index_geo ON tweets USING gist(geo);
CREATE INDEX tweets_index_withheldincountries ON tweets USING gin(withheld_in_countries);
CREATE TABLE tweet_urls (
        id_tweets BIGINT,
        url TEXT
    );

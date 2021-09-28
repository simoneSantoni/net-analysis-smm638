# Final course project (on homophily, closure, and performance)– README

<!-- TOC -->

- [Final course project (on homophily, closure, and performance)– README](#final-course-project-on-homophily-closure-and-performance-readme)
- [Introduction](#introduction)
- [Problem to address](#problem-to-address)
- [Background for the case study](#background-for-the-case-study)
- [Data](#data)
  - [Dataset 1 – technology supply network in Formula 1](#dataset-1--technology-supply-network-in-formula-1)
    - [Source](#source)
    - [Data tables](#data-tables)
    - [Data analysis tips](#data-analysis-tips)
  - [Dataset 2 – founding teams in the UK economy](#dataset-2--founding-teams-in-the-uk-economy)
    - [Source](#source-1)
    - [Data tables](#data-tables-1)
    - [Data analysis tips](#data-analysis-tips-1)
  - [Dataset 3 – mobility network among professional football players](#dataset-3--mobility-network-among-professional-football-players)
    - [Source](#source-2)
    - [Data tables](#data-tables-2)
    - [Data analysis tips](#data-analysis-tips-2)
  - [Dataset 4 – collaboration and performance in hip hop music](#dataset-4--collaboration-and-performance-in-hip-hop-music)
    - [Source](#source-3)
    - [Data tables](#data-tables-3)
    - [Data analysis tips](#data-analysis-tips-3)
- [Deliverables](#deliverables)

<!-- /TOC -->

<center>
<img src='images/similarity.jpg' width=600px/>

<b> Figure 1:</b>
An example of homophily from cultural markets: 'Family Guy' and 'The Simpsons' as products that foot each other in the market
</center>

# Introduction

This final course project deals with the topics of homophily, closure, and
performance. There is consistent evidence that selection and socialization
mechanisms – as the vessels of homophily – vastly affect entities' choices
such as partner selection, hiring, collaboration, or consumption. What is less
clear is how selection and socialization impact an entity's performance by
influencing the decision making process (see Figure 2).

<center>
<img src='images/homophily_performance.jpg' width=600px/>

<b> Figure 2:</b>
The causal path between homophily and performance from the perspective of an
 individual entity (e.g., a job seeker)
</center>

# Problem to address

Focus on one of the datasets described in the [Data](#data) section and
address the following questions:

- (to what extent) is homophily present in the network dataset at hand?
- then, how does homophily relate to entity's performance?

# Background for the case study

To deliver the project, students may want to rely upon the following concepts
and tools:

- theoretical concept of homophily
- homophily-related network mechanisms: selection and socialization
- empirical implementations of the homophily framework

In terms of the program of SMM638, all 'week 4' materials could be relevant.

# Data

Students are allowed to pick-up __one__ network dataset among:

1. technology supply network in Formula 1
2. founding teams in the UK economy
3. mobility network among professional football players
4. collaboration network among hip hop artists

## Dataset 1 – technology supply network in Formula 1

<center>
<img src='images/ferrari.jpg' width=600px/>

<b>Figure 3:</b> 'La Rossa' - the single and only one
</center>

### Source

Data have been manually coded from the book series ['Who Works in Formula 1'](https://whoworkssportsguides.com/). Data tables are stored in this [shared Google Drive folder](https://drive.google.com/drive/folders/12qMZEdVbLfTxdp0UNawFrmXKPOeuI0HL?usp=sharing).

### Data tables

 Here is the codebook of the variable by data table:

- `f1team_demography.json`:
  - `team`: name of the F1 team
  - `team_id`: ID for F1 team (don't be surprised to see the same ID applies to F1 team with different names - sometimes, teams change name/sponsor while ownership doesn't)
- `supplier_component_demography.json`:
  - `name`: name of the supplier of technology (e.g., car engine)
  - `team_id`: ID for the supplier of technology
- `component_demography.json`: dictionary of car components mapping onto the next table `f1team_supplier_network.json`. An F1 car contains thousands of components that can be grouped into 8 categories (aerodynamics, chassis, electronics, engine components, mechanics, wheels, engine, tyres)
- `f1team_supplier_network.json`:
  - `team_id`: ID for F1 team
  - `year`: F1 season
  - `supplier_id`: ID for the supplier
  - `comp_id`: category of component supplied/sourced
- `race_results.json` (organized around gp-driver-team triplets):
  - `gp`: grand-prix
  - `position`: final position of the driver
  - `driver` : driver
  - `laps` : laps completed
  - `n` : drivers completing the race
  - `points` : standing points
  - `race_outcome` : race outcome (qualitative variable)
  - `time` : time necessary to complete the race
  - `average_speed` : average speed
  - `technical_retirement` : technical retirements (binary variable)
  - `collision` : car collision (binary variable)
  - `accident` : car accident (binary variable)
  - `technical_rules_infringement` : technical rule infringement (binary variable)
  - `race_rules_infringement` : race rule infringement (binary variable)
  - `total_laps` : totale laps
  - `team_id` : ID for the F1 team  
  - `failed_comp_id` : failed component (it presents some missing values – sometimes, the reasons for technical retirement are not clear)

### Data analysis tips

Students may want to:

- consider the supplier - F1 team collaboration network as a two-mode, supply network
- use some race-level outcome as performance measure
- emphasize the role of focal and membership closure in predicting the formation of inter-organizational ties linking suppliers and F1 teams

## Dataset 2 – founding teams in the UK economy

<center>
<img src='images/startupper.jpg' width=600px/>

<b>Figure 4:</b> image of a startupper (or a student...who knows...)
</center>

### Source

Data come from the archives of Companies House. Regarding data access:

- company-level data on UK-based businesses can be retrieved from the archived of [Free Company Data Product](http://download.companieshouse.gov.uk/en_output.html)
- founder-level data can be retrieved from the archive [People with
  significant control(PSC)](http://download.companieshouse.gov.uk/en_pscdata.html) snapshot

### Data tables

Key information about the data and users guidance are available in the
[Companies
House](https://www.gov.uk/guidance/companies-house-data-products#comp-data)
website and in this [companion
document](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/426891/uniformResourceIdentifiersCustomerGuide.pdf).

### Data analysis tips

Students may want to:

- consider the [People with significant control
  (PSC)](http://download.companieshouse.gov.uk/en_pscdata.html) snapshot as
  a two-mode network linking people and companies via the 'significant control'
  relation (see below-displayed screenshot)
- to make the data manageable:
  - focus on selected sectors (i.e., a sample of SIC codes)
  - focus on a local economy (e.g., London)
- to build a meaningful performance variable:
  - focus on recently created companies
  - consider the variable `CompanyStatus` – status values such as `Active -  
    Proposal to Strike off` or  `Liquidation` are associated with company
    failure

```{json}
{'company_number': '09145694',
 'data': {'address': {'address_line_1': 'St. Andrews Road',
   'country': 'England',
   'locality': 'Henley-On-Thames',
   'postal_code': 'RG9 1HP',
   'premises': '2'},
  'ceased_on': '2018-05-14',
  'country_of_residence': 'England',
  'date_of_birth': {'month': 2, 'year': 1977},
  'etag': '3b8caf795c03af63921e381f7bb8300a51ebb73d',
  'kind': 'individual-person-with-significant-control',
  'links': {'self': '/company/09145694/persons-with-significant-control/individual/bIhuKnMFctSnjrDjUG8n3NgOrlU'},
  'name': 'Mrs Nga Thanh Wildman',
  'name_elements': {'forename': 'Nga',
   'middle_name': 'Thanh',
   'surname': 'Wildman',
   'title': 'Mrs'},
  'nationality': 'Vietnamese',
  'natures_of_control': ['ownership-of-shares-50-to-75-percent'],
  'notified_on': '2016-04-06'}}
```

<center>
<b>
Figure 3:
</b>
sample record from the 'People with significant control(PSC)' snapshot
</center>

## Dataset 3 – mobility network among professional football players

<center>
<img src='images/eriksen.jpg' width=400px/>

<b>Figure 5:</b> poor Eriksen or poor Inter Milan fans?
</center>

### Source

The Github repo [`ewenme/trasnfers`](https://github.com/ewenme/transfers)
contains updated, longitudinal data on moves involving male professional
football players in the major European championships.

There are several publicly available datasets covering professional championships, and ,especially, [Transfermarket](https://www.transfermarkt.com/)– students are welcome to use the datasets they prefer.

### Data tables

Data are offered as a collection of flat .csv files (i.e., there's one .csv per championship & season).

### Data analysis tips

Students may want to:

- consider the set of mobility events of the below-displayed as:
  - career spells - two data-points concerning a certain player `j` indicate when `i` started to play for team `j` and for how long he has been playing for team `j` before joining team `k`
  - a two-mode (affiliation network) linking players `{1, 2, ..., i,..., N}` and teams (from career spells, it's straightforward that Romelu Lukaku has played for Man Utd in seasons 2017-2018 and 2019-2020
- look at the 'fee' variable as a proxy of player performance (the fee team `k` pays to team `j` is the actualized flow of future performance of a player). That said, students are certainly allowed to expand their analyses by taking into account further variables such as team performance (e.g., standings, easy to collect) or player performance (goals work fine for strikers only! ;-)). Collecting further data is not mandatory though
- both projections of the two-mode network could be interesting to analyze:
  - one captures the inter-organizational pipes (e.g., `Everton <-> Man Utd`) that emerge as players engage in mobility
  - the other captures the social ties that develop among teammates (btw, do players pay for playing with former teammates?)

```{json}
{'club_name':	'Inter Milan',
 'player_name': 'Romelu Lukaku',
 'age':	26,
 'position': 'Centre-Forward',
 'club_involved_name': 'Man Utd',
 'fee': '£66.60m',
 'transfer_movement': 'in',
 'transfer_period':	'Summer',
 'fee_cleaned':	66.6,
 'league_name': 'Serie A',
 'year': 2019,
 'season': '2019/2020'
}
```
<center>
<b>Figure 6:</b> sample record from `ewenme/transfers` repo
</center>

## Dataset 4 – collaboration and performance in hip hop music

<center>
<img src='images/juiceWRLD.jpg' width=400px/>

<b>Figure 7:</b> [Juicy WRLD](https://soundcloud.com/uiceheidd)
</center>

### Source

Data have been downloaded from Billboard and Spotify. Particularly, I went through the following steps:

- I sampled all artists with at least one occurrence in the [Hot RB/Hip-Hop Songs](https://www.billboard.com/charts/r-b-hip-hop-songs) over the Jan 1 2018 - Nov 21 2020 timespanExhaustive documentation
- I identified a set of 353 unique artists, 341 of which have at least one album in Spotify (the remaining artists part-take in songs as collaborators only)
- then, I retrieved all albums for each of the 341 artist
- then, I retrieved all tracks for each album identified in the previous step

### Data tables

The various data tables are available for download from the following [Google Drive folder](https://drive.google.com/drive/folders/1jHQEExqZBnhips3CIM5C11pkr5Mfmq0P?usp=sharing).

Billboard data (see `rb_hp_chart.json`) are included in a flat file with the following structure:

```{json}
{
    "_id" : ObjectId("5fbbda647592682417920ffd"),
    "chart" : "r-b-hip-hop-songs",
    "date" : ISODate("2018-01-06T00:00:00.000+0000"),
    "rank" : NumberInt(1),
    "title" : "Rockstar",
    "artist" : "Post Malone Featuring 21 Savage",
    "weeks" : NumberInt(15),
    "peak" : NumberInt(1),
    "new" : false
}
```
<center>
<b>Figure 8:</b> sample record from `rb_hp_chart.json` file
</center>

Concerning the substantive fields included in the file:

- `title` is the title of the track
- `artist` is the artist's name
- `weeks` is a time variant variable that indicates the weeks elapsed since the inclusion of the track in the chart
- `peak` is a time variant variable the indicates the highest rank of the track in the chart

The tables/variables included in the Spotify data data are well documented in
the [Web API reference guide of the API service](https://developer.spotify.com/documentation/web-api/). In terms of files, `artists.json` contains the set of artists along with their attributes; `albums.json` contains the set of albums (nested within artists) along with their attributes; `tracks.json` contains the set of tracks (nested within albums) along with their attributes.

### Data analysis tips

Students may want to:

- consider the inclusion of a track in the Hot RB/Hip-Hop Songs chart, the `wweks`, and the `peak` variables as measures of commercial performance of the track
- consider the `artists` section of the `tracks.json` file as a source of relational data. As per the below-displayed example, Kanye West and Syleena Johnson collaborate to create the 'All Falls Down' single included in the acclaimed West's 'College Dropout' album
- the projection of the two-mode, collaborative network included in the `artists` can be purposefully projected to represent the social interactions among artists
- the `json_normalize` function from the Pandas library can be an important ally to effectively and efficiently set-up the data for the analyses.

```{json}
"artists" : [
    {
        "external_urls" : {
            "spotify" : "https://open.spotify.com/artist/5K4W6rqBFWDnAN6FQUkS6x"
        },
        "href" : "https://api.spotify.com/v1/artists/5K4W6rqBFWDnAN6FQUkS6x",
        "id" : "5K4W6rqBFWDnAN6FQUkS6x",
        "name" : "Kanye West",
        "type" : "artist",
        "uri" : "spotify:artist:5K4W6rqBFWDnAN6FQUkS6x"
    },
    {
        "external_urls" : {
            "spotify" : "https://open.spotify.com/artist/1lE6SEy8f84Zhjvp7r8yTD"
        },
        "href" : "https://api.spotify.com/v1/artists/1lE6SEy8f84Zhjvp7r8yTD",
        "id" : "1lE6SEy8f84Zhjvp7r8yTD",
        "name" : "Syleena Johnson",
        "type" : "artist",
        "uri" : "spotify:artist:1lE6SEy8f84Zhjvp7r8yTD"
    }
],
```

<center>
<b>Figure 9:</b> sample record from `tracks.json` file (`artists` section)
</center>

# Deliverables

Students are required to submit:

1. a 10-frame slideshow that illustrate the managerial implications of the work
2. the code/data necessary to reproduce the tables/visualizations included in the slideshow
3. a companion document that explains the background for the analyses (e.g., literature, white papers, technical reports, estimation choices)

Upload the slideshow via Moodle by December 17 (16:00).

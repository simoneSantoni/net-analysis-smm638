# SoundCloud Network Analytics Dataset

## Overview

This dataset represents a SoundCloud-like music streaming platform with a two-layer network structure: a social network layer (users following users) and a content layer (tracks), with cross-layer interactions (users engaging with tracks).

**Dataset Scale:**
- **Users:** 8,000 total
  - Listeners only: ~6,400 (80%)
  - Creators (upload content): ~1,600 (20%)
  - Hybrid users included in creator count
- **Tracks:** 15,000
- **Follows:** ~60,000 edges (avg degree ~15)
- **Engagements:** ~150,000 (likes, reposts, comments)
- **Streaming Events:** ~500,000 (sampled)
- **Time Period:** 12 months (January 2020 - December 2020)

## Data Files

### 1. users.csv

User profiles including both listeners and creators.

**Schema:**
```
user_id,username,user_type,join_date,follower_count,following_count,track_count,total_plays
```

**Fields:**
- `user_id` (string): Unique identifier (format: U000001-U008000)
- `username` (string): Display name (format: user_####)
- `user_type` (string): One of ["listener", "creator", "curator"]
  - listener: Only consumes content
  - creator: Uploads tracks (may also listen)
  - curator: High-activity listener who creates playlists
- `join_date` (date): Account creation date (YYYY-MM-DD)
- `follower_count` (int): Number of followers (computed)
- `following_count` (int): Number of users followed (computed)
- `track_count` (int): Number of tracks uploaded (0 for listeners)
- `total_plays` (int): Total plays received across all tracks (0 for listeners)

**Distribution:**
- User types: 70% listener, 25% creator, 5% curator
- Join dates: Exponential growth from 2019-01 to 2020-12
- Activity follows power law (few super-active users)

---

### 2. tracks.csv

Content catalog with metadata.

**Schema:**
```
track_id,creator_id,title,upload_date,duration_sec,genre_primary,genre_secondary,play_count,like_count,repost_count,comment_count
```

**Fields:**
- `track_id` (string): Unique identifier (format: T000001-T015000)
- `creator_id` (string): Reference to users.user_id
- `title` (string): Track name (format: Track_####_by_username)
- `upload_date` (date): When track was uploaded (YYYY-MM-DD)
- `duration_sec` (int): Track length in seconds (120-360, avg 180)
- `genre_primary` (string): Primary genre tag
- `genre_secondary` (string): Secondary genre tag (nullable)
- `play_count` (int): Total number of plays
- `like_count` (int): Total likes received
- `repost_count` (int): Total reposts received
- `comment_count` (int): Total comments received

**Genres:**
- Electronic (subgenres: House, Techno, Dubstep, Drum & Bass)
- Hip-Hop (subgenres: Trap, Lo-Fi, Boom Bap, SoundCloud Rap)
- Indie (subgenres: Indie Pop, Indie Rock, Dream Pop)
- Ambient (subgenres: Chillwave, Downtempo)
- Pop
- R&B
- Rock
- Jazz

**Distribution:**
- Creator productivity: Pareto distribution (few prolific creators)
- Genre clustering: Community-based (creators tend to stay in genre)
- Quality variation: Play counts follow power law (few viral hits)

---

### 3. follows.csv

Social network edges (who follows whom).

**Schema:**
```
follower_id,followee_id,follow_date
```

**Fields:**
- `follower_id` (string): User who follows (reference to users.user_id)
- `followee_id` (string): User being followed (reference to users.user_id)
- `follow_date` (date): When follow relationship was created (YYYY-MM-DD)

**Network Properties:**
- Directed graph
- Scale-free structure (Barabási-Albert preferential attachment)
- Average degree: ~15
- Clustering coefficient: 0.15-0.25 (typical for social networks)
- Community structure: Genre-based homophily (users follow others with similar taste)
- Temporal dynamics: Follow relationships grow over time

---

### 4. engagements.csv

User interactions with tracks (likes, reposts, comments).

**Schema:**
```
engagement_id,user_id,track_id,engagement_type,timestamp,comment_text
```

**Fields:**
- `engagement_id` (string): Unique identifier (format: E000001-E150000)
- `user_id` (string): User who engaged (reference to users.user_id)
- `track_id` (string): Track engaged with (reference to tracks.track_id)
- `engagement_type` (string): One of ["like", "repost", "comment"]
- `timestamp` (datetime): When engagement occurred (YYYY-MM-DD HH:MM:SS)
- `comment_text` (string): Comment content (nullable, only for type=comment)

**Distribution:**
- Engagement ratio: 60% like, 30% repost, 10% comment
- Temporal clustering: Viral tracks get burst of engagement
- Network effects: Users engage with tracks from followed creators 3x more
- Recency bias: New tracks get more engagement in first 7 days

---

### 5. streaming_events.csv

Listening behavior sample (not exhaustive, sampled for analysis).

**Schema:**
```
stream_id,user_id,track_id,start_time,duration_played_sec,completion_rate,source
```

**Fields:**
- `stream_id` (string): Unique identifier (format: S000001-S500000)
- `user_id` (string): Listener (reference to users.user_id)
- `track_id` (string): Track played (reference to tracks.track_id)
- `start_time` (datetime): When playback started (YYYY-MM-DD HH:MM:SS)
- `duration_played_sec` (int): How long user listened
- `completion_rate` (float): Percentage of track played (0.0-1.0)
- `source` (string): Discovery mechanism ["feed", "search", "repost", "playlist", "profile", "recommendation"]

**Distribution:**
- Completion rate: Beta distribution (most users finish or skip quickly)
- Source distribution:
  - feed: 35% (main timeline)
  - repost: 25% (viral spread)
  - profile: 20% (direct creator visit)
  - recommendation: 10% (algorithmic)
  - playlist: 7%
  - search: 3%
- Temporal patterns: Activity peaks evenings/weekends

---

### 6. playlists.csv

User-curated track collections.

**Schema:**
```
playlist_id,creator_id,playlist_name,creation_date,track_ids,follower_count
```

**Fields:**
- `playlist_id` (string): Unique identifier (format: P00001-P01000)
- `creator_id` (string): User who created playlist (reference to users.user_id)
- `playlist_name` (string): Playlist title
- `creation_date` (date): When playlist was created (YYYY-MM-DD)
- `track_ids` (string): Comma-separated list of track IDs
- `follower_count` (int): Number of users following the playlist

**Distribution:**
- ~1,000 playlists total
- Created by curators (60%) and creators (40%)
- Average playlist size: 15-30 tracks
- Genre coherence: 70% of tracks in playlist share primary genre
- Some playlists become influential (high follower count)

---

## Network Properties

### Social Network (Follows)

**Characteristics:**
- Scale-free structure with power-law degree distribution
- Small-world property (short average path length)
- High clustering within genre communities
- 8 genre-based communities with varying connectivity
- Early users often become influential hubs

### Content Network (Tracks → Creators)

**Structure:**
- Bipartite network linking creators to their tracks
- Creator productivity varies significantly (some very prolific)
- Genre specialization patterns (creators often focus on 1-2 genres)

### Engagement Network (Users → Tracks)

**Dynamics:**
- Network effects amplify engagement (users engage 3x more with followed creators)
- Viral spread through repost cascades
- Temporal patterns (new content gets more initial engagement)

## Platform Evolution

**Time Period:** 2020-01-01 to 2020-12-31

**Key Patterns:**
- Continuous user growth throughout the year
- Steady content upload patterns
- Evolution of follow relationships and community structures
- Viral content cascades and engagement patterns
- Playlist creation and curation activities

## Statistical Properties Summary

| Metric | Value |
|--------|-------|
| Users | 8,000 |
| Creators | 1,600 (20%) |
| Tracks | 15,000 |
| Follow edges | ~60,000 |
| Avg follows per user | 15 |
| Network clustering | 0.15-0.25 |
| Communities | 8 (genre-based) |
| Engagements | ~150,000 |
| Streaming events | ~500,000 |
| Playlists | ~1,000 |
| Time period | 12 months |

## Pedagogical Use Cases

This dataset supports:

1. **Basic Network Analysis**
   - Degree distributions and centrality measures
   - Community detection algorithms
   - Path analysis and network diameter

2. **Recommendation Systems**
   - Collaborative filtering (user-user, item-item)
   - Network-based recommendations (friends' tracks)
   - Hybrid approaches (content + network)

3. **Influence & Viral Spread**
   - Identifying taste-makers (high centrality creators)
   - Tracking repost cascades
   - Measuring content reach

4. **Strategic Analysis**
   - Comparing discovery sources (feed vs. recommendation)
   - Evaluating network effects on engagement
   - Community structure analysis for genre evolution

5. **Temporal Analysis**
   - Growth patterns over time
   - Early adopter advantages
   - Content lifecycle (upload → viral → decay)

## Data Formats

Data is available in:
- **CSV** - Universal format, easy to load in Python/R
- **GraphML** - For network analysis tools (Gephi, Cytoscape)
- **JSON** - For web applications and APIs
- **NetworkX pickle** - For Python-based analysis

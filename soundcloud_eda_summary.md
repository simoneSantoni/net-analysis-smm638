# SoundCloud Data EDA Summary

## Dataset Overview
The SoundCloud dataset contains information about users, tracks, social connections, and engagement patterns from 2019-2020, with a focus on hip-hop music.

## Key Statistics

### Users (8,000 total)
- **User Types**: 75% listeners (6,000), 20% creators (1,600), 5% curators (400)
- **Average follower/following count**: 7.5 users
- **Join period**: January 2019 - December 2020
- **Track production**: Only creators produce tracks (avg 1.875 tracks per user overall)

### Tracks (15,000 total)
- **Upload period**: January 2020 - December 2020
- **Duration**: Average 185 seconds (3 minutes), ranging from 2-6 minutes
- **Play counts**: Average 33 plays per track (11-68 range)
- **Engagement rates**: ~18% like rate (6 likes per 33 plays), ~9% repost rate
- **Top genres**: Hip-hop dominates with Trap (16.7%), Alternative Hip-Hop (16.6%), Boom Bap (16.6%), Lo-Fi (16.3%), and SoundCloud Rap (15.9%)

### Social Network (60,000 follow relationships)
- **Network density**: 7,995 unique followers connecting to 7,998 unique users
- **Most followed users**: Top accounts have 18-20 followers
- **Average out-degree**: 7.5 (matches overall following count)

### User Engagement (150,000 events)
- **Types**: 60% likes (89,915), 30% reposts (45,180), 10% comments (14,905)
- **Participation**: All 8,000 users engaged with content
- **Coverage**: 14,999 out of 15,000 tracks received engagement
- **Average activity**: 18.8 engagements per user

### Streaming Behavior (500,000 events)
- **Active users**: 7,997 unique streamers
- **Track coverage**: 14,990 tracks were streamed
- **Listen duration**: Average 88 seconds (48% completion rate)
- **Discovery sources**: 44% direct, 36% playlists, 20% reposts

### Playlists (1,000 total)
- **Creators**: 994 unique playlist creators
- **Size**: Average 50 tracks per playlist
- **Popularity**: Low follower counts (avg 1 follower)

## Key Insights

1. **User Distribution**: The platform shows a healthy 4:1 listener-to-creator ratio with a small but active curator community.

2. **Content Focus**: Strong hip-hop orientation with five main subgenres dominating 81% of content.

3. **Engagement Patterns**: High engagement-to-play ratio suggests an active, invested community rather than passive consumption.

4. **Network Structure**: Relatively egalitarian follow distribution (no extreme influencers in this sample).

5. **Discovery Mechanisms**: Mixed discovery with direct access leading, but significant playlist and repost-driven discovery.

6. **Listening Behavior**: 48% average completion rate indicates users actively browse/sample rather than full listens.

## Visualizations Generated
- `follower_distribution.png`: Log-scale distribution of follower counts
- `playback_distribution.png`: Track play count distribution
- `engagement_types.png`: Breakdown of like/repost/comment activities
- `user_types.png`: User type distribution
- `top_genres.png`: Top 20 music genres
- `streaming_sources.png`: How users discover tracks
- `combined_overview.png`: 4-panel summary visualization

## Files Analyzed
- users.csv (8,000 records)
- tracks.csv (15,000 records)
- follows.csv (60,000 records)
- engagements.csv (150,000 records)
- streaming_events.csv (500,000 records)
- playlists.csv (1,000 records)
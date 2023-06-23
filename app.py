import streamlit as st
from instaloader import Instaloader, Profile

def calculate_engagement_rate(likes, comments, followers, posts):
    engagement_rate = (likes + comments) / (followers * posts) * 100
    return engagement_rate

def get_instagram_stats(username, top_posts_count=5):
    loader = Instaloader()
    profile = Profile.from_username(loader.context, username)
    
    num_followers = profile.followers
    total_likes = 0
    total_comments = 0
    total_posts = 0
    top_posts = []
    
    for post in profile.get_posts():
        total_likes += post.likes
        total_comments += post.comments
        total_posts += 1
        if len(top_posts) < top_posts_count:
            top_posts.append({'url': post.url, 'likes': post.likes, 'comments': post.comments})
    
    engagement_rate = calculate_engagement_rate(total_likes, total_comments, num_followers, total_posts)
    estimated_reach = (total_likes + total_comments) / total_posts
    potential_impact = engagement_rate * num_followers
    potential_reach = estimated_reach * num_followers
    influence = potential_impact + potential_reach
    average_likes_per_post = total_likes / total_posts
    
    return {
        'username': username,
        'posts': total_posts,
        'followers': num_followers,
        'engagement_rate': engagement_rate,
        'estimated_reach': estimated_reach,
        'total_likes': total_likes,
        'total_comments': total_comments,
        'potential_impact': potential_impact,
        'potential_reach': potential_reach,
        'influence': influence,
        'average_likes_per_post': average_likes_per_post,
        'top_posts': top_posts
    }

def main():
    st.title("Instagram Stats")
    username = st.text_input("Enter Instagram username:")
    
    if st.button("Get Stats"):
        stats = get_instagram_stats(username)
        
        st.subheader(f"Username: {stats['username']}")
        st.write(f"Posts: {stats['posts']}")
        st.write(f"Followers: {stats['followers']}")
        st.write(f"Engagement Rate: {stats['engagement_rate']:.2f}%")
        st.write(f"Estimated Reach: {stats['estimated_reach']:.2f}")
        st.write(f"Total Likes: {stats['total_likes']}")
        st.write(f"Total Comments: {stats['total_comments']}")
        st.write(f"Potential Impact: {stats['potential_impact']}")
        st.write(f"Potential Reach: {stats['potential_reach']}")
        st.write(f"Influence: {stats['influence']}")
        st.write(f"Average Likes per Post: {stats['average_likes_per_post']:.2f}")
        
        st.subheader("Top Posts:")
        for i, post in enumerate(stats['top_posts']):
            st.write(f"\nPost {i+1}:")
            st.write(f"URL: {post['url']}")
            st.write(f"Likes: {post['likes']}")
            st.write(f"Comments: {post['comments']}")

if __name__ == '__main__':
    main()

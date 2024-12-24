// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MiniTwitter {

    struct Post {
        string message;
        address author;
        uint256 likes;
        uint256 dislikes;
        uint256 timestamp;
        uint256 lastModified;
    }

    Post[] public posts;

    // Publish a new post
    function publishPost(string memory _message) public {
        Post memory newPost = Post({
            message: _message,
            author: msg.sender,
            likes: 0,
            dislikes: 0,
            timestamp: block.timestamp,
            lastModified: block.timestamp
        });
        posts.push(newPost);
    }

    // Get a post by index
    function getPost(uint256 index) public view returns (string memory, address, uint256, uint256, uint256, uint256) {
        require(index < posts.length, "Index out of bounds");
        Post storage post = posts[index];
        return (post.message, post.author, post.likes, post.dislikes, post.timestamp, post.lastModified);
    }

    // Like a post
    function likePost(uint256 index) public {
        require(index < posts.length, "Post does not exist");
        posts[index].likes++;
    }

    // Dislike a post
    function dislikePost(uint256 index) public {
        require(index < posts.length, "Post does not exist");
        posts[index].dislikes++;
    }

    // Edit a post by the owner
    function editPost(uint256 index, string memory _newMessage) public {
        require(index < posts.length, "Post does not exist");
        Post storage post = posts[index];
        require(post.author == msg.sender, "Only the owner can edit this post");

        post.message = _newMessage;
        post.lastModified = block.timestamp;
    }

    // Get the total number of posts
    function getTotalPosts() public view returns (uint256) {
        return posts.length;
    }
}

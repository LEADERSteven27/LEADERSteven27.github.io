var posts=["2025/07/14/hello-world/","2025/07/15/动物朋友/","2025/07/17/微观经济学/","2025/07/15/文献综述与科技写作/","2025/07/15/计算机视觉/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };
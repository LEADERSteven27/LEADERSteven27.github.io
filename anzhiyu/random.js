var posts=["2025/07/17/微观经济学绪论/","2025/07/15/计算机视觉概述/","2025/07/15/文献综述与科技写作/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };
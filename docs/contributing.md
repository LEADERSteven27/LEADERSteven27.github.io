# 贡献指南

这个站点目前主要由个人维护，但内容最好保持可持续更新。

## 写作约定

- 每门课程使用 `docs/<分类>/<课程>/index.md` 的目录形式。
- 课程页面尽量套用 [课程页面模板](template.md)。
- 文件名使用英文或拼音，页面标题使用中文。
- 大文件资料不要直接放入仓库，优先使用外部链接或云盘。

## 本地预览

``` powershell
python -m pip install -r requirements.txt
mkdocs serve
```

## 构建检查

``` powershell
mkdocs build --strict
```

构建通过后再提交，能少很多发布时的意外。


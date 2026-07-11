# Chasing The Light

个人课程笔记、学习资料与知识库站点，基于 Material for MkDocs。

## 目录结构

- `mkdocs.yml`：站点主题、插件和构建配置，不写长导航。
- `docs/.pages`：顶层栏目顺序。
- `docs/<栏目>/.pages`：栏目内课程顺序。
- `docs/<栏目>/index.md`：栏目说明和课程清单。
- `docs/<栏目>/<课程>/index.md`：具体课程笔记。
- `templates/course.md`：新课程页模板。
- `scripts/scaffold_course_pages.py`：补齐培养方案中的课程占位页。
- `site/`：构建产物，已被 `.gitignore` 忽略。

## 写一篇课程笔记并发布

1. 先同步远端，避免覆盖线上已有改动：

```powershell
git pull origin main
```

2. 在对应栏目中找到课程目录，例如 `docs/required/applied-optics/index.md`。
3. 直接编辑这个 `index.md`，保留标题和必要的课程元数据即可。
4. 如果是新课程，复制 `templates/course.md` 到 `docs/<栏目>/<课程英文名>/index.md`。
5. 新课程会自动出现在侧边栏；如需调整顺序，编辑该栏目的 `.pages`。
6. 本地检查：

```powershell
python -m pip install -r requirements.txt
python -m mkdocs build --strict
```

7. 本地预览：

```powershell
python -m mkdocs serve --dev-addr=127.0.0.1:8000
```

8. 检查改动：

```powershell
git status
git diff
```

9. 提交并推送：

```powershell
git add -A
git commit -m "Add note: 笔记标题"
git push origin main
```

10. 等待 GitHub Actions 完成发布，再刷新线上页面。若浏览器仍显示旧页面，强制刷新或给 URL 加 `?v=提交号`。

## 更新栏目

1. 新增顶层栏目：在 `docs/` 下建目录，添加 `index.md` 和 `.pages`。
2. 调整顶层顺序：编辑 `docs/.pages`。
3. 调整某个栏目内课程顺序：编辑对应目录下的 `.pages`。
4. 不要手动修改或提交 `site/`。

## 添加 PDF 或图片

1. 优先把资源放在对应页面旁边的 `assets/` 目录，例如：
   - `docs/required/electromagnetic-fields/assets/electromagnetic-fields-notes.pdf`
   - `docs/required/electromagnetic-fields/assets/field-lines.png`
2. 在 Markdown 中使用相对链接：

```markdown
[手写笔记 PDF](assets/electromagnetic-fields-notes.pdf)
![场线示意图](assets/field-lines.png)
```

3. 一般不需要图床。课程笔记中的普通图片直接放仓库最省心。
4. 只有图片或 PDF 很大、数量很多、需要外链复用，或接近 GitHub 单文件 100 MB 限制时，再考虑图床、对象存储或网盘。

## 修改网页任意位置

1. 先判断你要改的是哪类内容：
   - 首页标题、入口卡片、更新记录：改 `docs/index.md`。
   - 某个栏目介绍或课程清单：改 `docs/<栏目>/index.md`。
   - 某门课的笔记正文：改 `docs/<栏目>/<课程>/index.md`。
   - 导航顺序：改对应目录的 `.pages`。
   - 字体、卡片、表格、间距等样式：改 `docs/stylesheets/custom.css`。
   - 站点名、仓库链接、主题功能、插件：改 `mkdocs.yml`。
2. 修改某个首页入口框里的文字：
   - 打开 `docs/index.md`。
   - 找到对应卡片，例如 `**[短学期课程](short_terms/index.md)**`。
   - 改它下面的 `<span class="card-desc">...</span>`。
3. 上传或新增一份课程笔记：
   - 如果课程页已经存在，直接编辑对应 `index.md`。
   - 如果课程页不存在，新建 `docs/<栏目>/<课程英文名>/index.md`，可从 `templates/course.md` 复制。
   - 新页面会自动进入侧边栏；需要调整顺序时再改该栏目 `.pages`。
   - 如果也希望它出现在栏目课程清单表格里，在 `docs/<栏目>/index.md` 增加一行链接。
4. 每次改完都运行：

```powershell
python -m mkdocs build --strict
```

5. 确认无误后提交并推送：

```powershell
git add -A
git commit -m "Update site content"
git push origin main
```

## 补齐课程占位页

如果误删了某个培养方案课程页，可以运行：

```powershell
python scripts/scaffold_course_pages.py
```

这只会创建缺失页面，不会覆盖已经写好的笔记。只有在确定要重置全部占位页时，才使用：

```powershell
python scripts/scaffold_course_pages.py --overwrite
```

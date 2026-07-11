# Genie Mountain

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

## 写一篇课程笔记

1. 在对应栏目中找到课程目录，例如 `docs/required/applied-optics/index.md`。
2. 直接编辑这个 `index.md`，保留标题和必要的课程元数据即可。
3. 如果是新课程，复制 `templates/course.md` 到 `docs/<栏目>/<课程英文名>/index.md`。
4. 新课程会自动出现在侧边栏；如需调整顺序，编辑该栏目的 `.pages`。
5. 本地检查：

```powershell
python -m pip install -r requirements.txt
python -m mkdocs build --strict
```

6. 本地预览：

```powershell
python -m mkdocs serve --dev-addr=127.0.0.1:8000
```

## 更新栏目

1. 新增顶层栏目：在 `docs/` 下建目录，添加 `index.md` 和 `.pages`。
2. 调整顶层顺序：编辑 `docs/.pages`。
3. 调整某个栏目内课程顺序：编辑对应目录下的 `.pages`。
4. 不要手动修改或提交 `site/`。

## 补齐课程占位页

如果误删了某个培养方案课程页，可以运行：

```powershell
python scripts/scaffold_course_pages.py
```

这只会创建缺失页面，不会覆盖已经写好的笔记。只有在确定要重置全部占位页时，才使用：

```powershell
python scripts/scaffold_course_pages.py --overwrite
```

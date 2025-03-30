import pandas as pd
from dataclasses import dataclass, asdict


@dataclass
class Comment:
    username: str
    date: str
    score_overall: str
    score_detail: str
    comment_text: str
    like: str
    # ip: str



def parse(html):
    """Parse fully-loaded comments from HTML object"""
    comment_list = html.css('div.list_item') # select comment list in fully-loaded html

    for item in comment_list: # 
        new_comment = Comment(
                username        = item.css_first('div.user_detail_name').text(strip=True), # 用户名
                date            = item.css_first("div.resource_date").text(strip=True).split()[0], # 评论日期
                score_overall   = item.css_first('div.score_content').text(strip=True), # 评分（最高5分）
                score_detail    = item.css_first("div.site_content").text(strip=True), # 评分细项：景色/趣味/性价比
                comment_text    = item.css_first('div.list_content').text(strip=True), # 评论全文
                like            = item.css_first('div.like_content').text(strip=True), # 点赞数
            )
        # print(new_comment)

        yield asdict(new_comment)



def write_csv(sight, results):
    """Write fully-loaded comments to csv"""
    df = pd.DataFrame(results, columns=Comment.__dataclass_fields__.keys())
    df.to_csv(f"../sights-comments/{sight}.csv", index=False)

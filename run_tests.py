import pytest
import os


# 创建报告目录
def ensure_report_dir():
    if not os.path.exists('reports'):
        os.makedirs('reports')


if __name__ == '__main__':
    ensure_report_dir()
pytest.main([
    'tests',
    '--junitxml=reports/report.xml',
    '--html=reports/report.html',
    '--self-contained-html'
])

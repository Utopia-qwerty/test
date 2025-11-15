pipeline {
agent any


environment {
PYTHON = "python3"
}


stages {
stage('Checkout') {
steps {
echo '拉取仓库代码...'
checkout scm
}
}


stage('Install Dependencies') {
steps {
echo '安装依赖...'
sh 'pip install -r requirements.txt'
}
}


stage('Run Tests') {
steps {
echo '执行自动化测试...'
sh 'python3 run_tests.py'
}
post {
always {
junit 'reports/*.xml'
}
}
}
}


post {
success { echo '构建成功！🎉' }
failure { echo '构建失败 ❌ 请检查日志' }
}
}

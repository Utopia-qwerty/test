pipeline {
    agent any

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
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo '执行测试...'
                bat 'python run_tests.py'
            }
        }
    }

    post {
        failure {
            echo '构建失败 ❌ 请检查日志'
        }
        success {
            echo '构建成功 🎉'
        }
    }
}

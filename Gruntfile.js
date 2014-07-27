module.exports = function(grunt) {
	// タスクの定義
	grunt.initConfig({
		// ファイル監視とブラウザの自動リロードの設定
		watch: {
			options: {
				interval: 1000
			},
			content: {
				files: [
					'hellodjango/**',
				],
				options: {
					livereload: true,
				}
			}
		}
	});

	// パッケージの自動読み込み
	var pkg = grunt.file.readJSON('package.json');
	var taskName;
	for (taskName in pkg.devDependencies) {
		if (taskName.substring(0, 6) == 'grunt-') {
			grunt.loadNpmTasks(taskName);
		}
	}

	// タスクの登録
	// default で登録したタスクは、grunt コマンドで実行される
	// dist で登録したタスクは、grunt dist　コマンドで実行される (デプロイ用)
	grunt.registerTask('default', ['watch'])
	grunt.registerTask('dist', [])
};

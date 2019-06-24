const path = require("path");

const src = path.join(__dirname, "static");
const dist = path.join(__dirname, "static/dist");

module.exports = {
	mode: "development", // "production"
	entry: path.resolve(src, "ts/aho.ts"),
	output: {
		filename: "index.bundle.js",
		path: dist
	},
	resolve: {
		modules: ["node_modules"],
		extensions: [".js", ".jsx", ".ts", ".tsx"]
	},
	module: {
		rules: [
			{
				test: /\.(js|jsx)$/,
				exclude: /node_modules/,
				use: "babel-loader"
			},
			{
				test: /\.(ts|tsx)$/,
				exclude: /node_modules/,
				use: "ts-loader"
			}
		]
	},
	// devtool: "cheap-module-eval-source-map"
	devtool: "inline-source-map"
};

import { Configuration } from "webpack";
import * as MiniCssExtractPlugin from "mini-css-extract-plugin";
import * as CssMinimizerPlugin from "css-minimizer-webpack-plugin";
import * as path from "path";

const config: Configuration = {
  entry: {
    theme: ["./src/theme.ts", "./src/scss/theme.scss"],
  },
  devtool: "source-map",
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
      {
        test: /\.(s[ac]ss|css)$/i,
        use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"],
      },
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js"],
  },
  output: {
    filename: "[name].min.js",
    path: path.resolve(path.dirname("."), "dist"),
    clean: true,
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].min.css",
    }),
  ],
  optimization: {
    minimizer: [new CssMinimizerPlugin(), "..."],
  },
  watchOptions: {
    ignored: ["**/node_modules"],
  },
};

export default config;

import $ from "jquery"
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import { Bar } from "./bar"

let bar = new Bar(12345);
$("#result").text("bar.getValue=" + bar.getValue());
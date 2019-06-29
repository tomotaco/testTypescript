import $ from "jquery"
import { Bar } from "./bar"

let bar = new Bar(12345);
$("#result").text("bar.getValue=" + bar.getValue());
import $ from "jquery"
import { Bar } from "./bar"

let bar = new Bar(123);
$("#result").text("bar.getValue=" + bar.getValue());

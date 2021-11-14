import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from "rxjs";
import { User} from "../../models/user";
import { global} from "../../shared/global";


@Injectable()
export class UserService{
  public url: string;

  constructor(public _http: HttpClient) {
    this.url = global.url;
  }

}

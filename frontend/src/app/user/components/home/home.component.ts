import { Component, OnInit } from '@angular/core';
import * as utils  from "../../../shared/utils";
import { Router, ActivatedRoute } from '@angular/router';
import { AuthService} from "../../../auth/auth.service";
import {ComicService} from "../../../comic/services/comic.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  user: any;
  tag: string = "";
  comics: any = []

  constructor(private _router: Router, private _authService: AuthService, private _route: ActivatedRoute, private  _comicService: ComicService) { }

  ngOnInit(): void {
    if(!this._authService.isLoggedIn())
      this._router.navigate(["/login"]);

    this.getParams();
    this.getComics()
  }

  getParams(){
    this._route.queryParams.subscribe(params => {
      this.tag = params['tag'];
    });
  }

  getComics(){
   this._comicService.get(this.tag).subscribe(
     response =>{
       this.comics = response;
       console.log(response);
     },
     error =>{
       console.error(error);
     }
   )
  }

}

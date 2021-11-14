import { Component, OnInit } from '@angular/core';
import * as utils  from "../../../shared/utils";
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  private user: any;

  constructor(private _router: Router) { }

  ngOnInit(): void {
    this.validateSession()
  }

  validateSession(): void{
    this.user = utils.getUserSession();

    if(!this.user)
      this._router.navigate(["/login"])
  }

}

import { Component, OnInit } from '@angular/core';
import * as utils  from "../../../shared/utils";
import { Router, ActivatedRoute } from '@angular/router';
import { AuthService} from "../../../auth/auth.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  private user: any;

  constructor(private _router: Router, private _authService: AuthService) { }

  ngOnInit(): void {
    if(!this._authService.isLoggedIn())
      this._router.navigate(["/login"]);
  }

}

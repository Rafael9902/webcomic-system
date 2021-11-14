import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup} from "@angular/forms";
import { AuthService} from "../../../auth/auth.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  credentialsForm = new FormGroup({
    email: new FormControl(''),
    password: new FormControl('')
  });

  constructor(private _authService: AuthService) {}

  ngOnInit(): void {}

  onSubmit(){
    this._authService.login(this.credentialsForm.value).subscribe({
      next(response){
        console.log(response);
      },
      error(msg){
        console.error(msg);
      }
    });
  }

}
